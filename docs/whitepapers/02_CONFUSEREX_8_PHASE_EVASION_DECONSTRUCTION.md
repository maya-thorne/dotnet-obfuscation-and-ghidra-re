# 🔬 ConfuserEx 8-Phase Protection & Defense Evasion Deconstruction
Author: Maya Thorne (Systems & Reverse Engineering Research)
License: MT-SRL

## 1. Overview of the Confuser.Core Protection Pipeline
ConfuserEx processes .NET assemblies through structured pipeline phases:
1. `Inspection`: Dependency graph extraction.
2. `BeginModule`: dnlib AST module allocation.
3. `Optimize`: CIL macro simplification.
4. `ProcessModule`: Sequential application of the 8 core protections.
5. `EndModule`: Native runtime helper injection.
6. `Writing`: PE serialization and hash recomputation.

## 2. In-Depth Analysis of the 8 Core Protections

### 2.1 Name Protection (`Confuser.Renamer`)
- Replaces identifiers with Unicode homoglyphs, zero-width joiners (`\u200D`), or invalid UTF-8 byte sequences.
- Bypasses static regex string searches while preserving internal type resolution.

### 2.2 Control Flow Protection (`Confuser.Protections/ControlFlow`)
- Flattens structured loops (`for`, `while`) into complex state machines governed by a single `switch` statement with predicate arithmetic.
- Injects dead blocks and opaque predicates, breaking decompiled control flow graphs (CFGs).

### 2.3 Constants Protection (`Confuser.Protections/Constants`)
- Encrypts all string and primitive constants into a single encrypted byte array.
- Injects a dynamic method initializer (`.cctor`) that decrypts elements at runtime upon first access.

### 2.4 Reference Proxy (`Confuser.Protections/ReferenceProxy`)
- Replaces direct calls to external APIs (`Process.Start`, `File.WriteAllBytes`) with dynamically created delegates (`DynamicMethod`).
- Eliminates standard IAT and MemberRef tracking in static analysis.

### 2.5 Anti-Tamper (`Confuser.Protections/AntiTamper`)
- Encrypts all method bodies in the PE file.
- Injects a native module initializer that decrypts method bodies in memory before the CLR JIT compiler executes them.

### 2.6 Anti-Dump (`Confuser.Protections/AntiDump`)
- Erases PE header structures in memory (`0x00` fill across `0x1000` bytes at ImageBase) to thwart memory dump utilities.

### 2.7 Anti-Debug (`Confuser.Protections/AntiDebug`)
- Spawns background worker threads continuously monitoring debugger flags (`Debugger.IsAttached`, `CheckRemoteDebuggerPresent`).

### 2.8 Invalid Metadata (`Confuser.Protections/InvalidMetadata`)
- Emits corrupted metadata tables designed specifically to crash reverse engineering tools like dnSpy and ILSpy.
