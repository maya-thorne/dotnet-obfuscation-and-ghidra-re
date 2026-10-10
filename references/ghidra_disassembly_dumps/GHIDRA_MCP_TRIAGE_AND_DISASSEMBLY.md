# 🔬 Ghidra MCP Binary Triage & Disassembly Forensic Report
Author: Maya Thorne (Systems & Reverse Engineering Research)
License: MT-SRL

## 1. Ghidra MCP Triage Analysis (`xorStub.exe`)
- **File Name**: `xorStub.exe`
- **File Size**: 217,600 bytes
- **Format**: PE32 (x86 32-bit Portable Executable)
- **Image Base**: `0x00400000`
- **Entry Point RVA**: `0x0003673A` (Raw Offset: `0x0003493A`)
- **Section Headers**:
  - `.text`: VA `0x00002000`, VSize `0x00034740`, RawPtr `0x00000200`, RawSize `0x00034800` (Entropy: 3.3589)
  - `.rsrc`: VA `0x00038000`, VSize `0x0000059C`, RawPtr `0x00034A00`, RawSize `0x00000600` (Entropy: 4.0535)
  - `.reloc`: VA `0x0003A000`, VSize `0x0000000C`, RawPtr `0x00035000`, RawSize `0x00000200` (Entropy: 0.1019)

## 2. Entry Point Disassembly (`_CorExeMain` Bootstrap Thunk)
```nasm
; Disassembled via Ghidra MCP re_disassemble_offset
0x0003493A:  FF 25 00 20 40 00    JMP DWORD PTR ds:[0x00402000]   ; Jump to mscoree.dll!_CorExeMain
0x00034940:  00 00                ADD byte ptr [eax], al
0x00034942:  00 00                ADD byte ptr [eax], al
0x00034944:  00 00                ADD byte ptr [eax], al
```

## 3. Themida / Native Virtualization VM Interpreter Loop Disassembly
In native protectors like Themida, VMProtect, and ArmDot Native, the original x86 instructions are converted to bytecode interpreted by a custom virtual machine dispatcher:
```nasm
; Themida / VMProtect Virtual Machine Dispatcher Loop
0x00451000:  PUSHAD                         ; Save full register state
0x00451001:  MOV ESI, DWORD PTR [EBP+0x08]  ; ESI = Virtual Instruction Pointer (VIP)
0x00451004:  LODSB                          ; AL = Virtual Opcode
0x00451005:  MOVZX EAX, AL
0x00451008:  JMP DWORD PTR [EDI+EAX*4]      ; Indirect jump to VM Handler Table
; VM Handler 0x14: Custom Addition
0x00451240:  POP EBX                        ; Pop operand B from virtual stack
0x00451241:  POP ECX                        ; Pop operand A from virtual stack
0x00451242:  ADD ECX, EBX                   ; Perform arithmetic
0x00451244:  PUSH ECX                       ; Push result back to virtual stack
0x00451245:  JMP 0x00451004                 ; Loop back to VIP fetch
```

## 4. Blue Team Detection Takeaway
- While the internal VM logic is heavily obfuscated, the **VM entry point sequence (`PUSHAD`, `LODSB`, indirect handler jump)** and **high section entropy (> 7.5)** create unmistakable deterministic signatures for EDR memory scanners and YARA rules.
