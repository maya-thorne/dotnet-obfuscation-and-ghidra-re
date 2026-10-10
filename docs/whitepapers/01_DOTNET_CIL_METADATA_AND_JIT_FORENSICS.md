# 🔬 .NET CIL Metadata Streams & JIT Compilation Forensics
Author: Maya Thorne (Systems & Reverse Engineering Research)
License: MT-SRL

## 1. The ECMA-335 Common Intermediate Language (CIL) Architecture
Programs compiled targeting the Microsoft .NET Common Language Runtime (CLR) do not compile directly to native machine code. Instead, the Roslyn compiler produces Common Intermediate Language (CIL/MSIL) stack-based bytecode encapsulated in an ECMA-335 CLI file format.

### 1.1 Physical Layout of the CLI File Header
Within the Portable Executable (PE) wrapper, Data Directory index 14 points to the `IMAGE_COR20_HEADER` structure:
```c
typedef struct _IMAGE_COR20_HEADER {
    DWORD                   cb;
    WORD                    MajorRuntimeVersion;
    WORD                    MinorRuntimeVersion;
    IMAGE_DATA_DIRECTORY    MetaData;
    DWORD                   Flags;
    union {
        DWORD               EntryPointToken;
        DWORD               EntryPointRVA;
    };
    IMAGE_DATA_DIRECTORY    Resources;
    IMAGE_DATA_DIRECTORY    StrongNameSignature;
    IMAGE_DATA_DIRECTORY    CodeManagerTable;
    IMAGE_DATA_DIRECTORY    VTableFixups;
    IMAGE_DATA_DIRECTORY    ExportAddressTableJumps;
    IMAGE_DATA_DIRECTORY    ManagedNativeHeader;
} IMAGE_COR20_HEADER;
```

## 2. CLI Metadata Root and Stream Anatomy
The `MetaData` directory points to the physical Metadata Root, beginning with the signature `0x424A5342` (`BSJB`):
1. **`#Strings` Stream**: Stores UTF-8 identifier names (type, method, parameter, and field names).
2. **`#US` (User String) Stream**: Stores UTF-16LE user-defined string literals.
3. **`#Blob` Stream**: Stores variable-length binary payloads (signatures, default values, marshaling specs).
4. **`#GUID` Stream**: Stores 128-bit GUID values.
5. **`#~` / `#-` Stream**: Stores compressed/uncompressed relational metadata tables (`TypeDef`, `MethodDef`, `MemberRef`, `CustomAttribute`).

## 3. Anti-Decompilation & "Invalid Metadata" Exploitation
Because standard decompilers (dnSpy, ILSpy, dotPeek) assume strict compliance with ECMA-335, obfuscators deliberately tamper with these streams:
- **Stream Overlap / Negative Offsets**: Placing `#~` stream start offsets that overlap `#Strings`. The Windows CLR JIT loader tolerates this, but static decompilers throw `BadImageFormatException` or crash with unhandled index out-of-range exceptions.
- **Corrupted Stream Count**: Specifying a high stream count while truncating the file header.
- **Empty Method Bodies**: Emitting `MethodDef` tokens with RVA pointing to unmapped memory, relying on a runtime JIT hook (AntiTamper) to synthesize bytecode dynamically.
