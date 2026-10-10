# 🔬 Native Packer Architectures, PE Overlays & Stub Reverse Engineering
Author: Maya Thorne (Systems & Reverse Engineering Research)
License: MT-SRL

## 1. PE Overlay Mechanics
The Portable Executable (PE) format defines section boundaries explicitly in the Section Table headers. Any data appended to the physical file beyond the `PointerToRawData + SizeOfRawData` of the final section is considered **PE Overlay**:
- The Windows OS PE loader ignores overlay bytes when mapping the executable into memory.
- However, self-reading executables (droppers, unpackers) open their own file on disk (`Assembly.GetEntryAssembly().Location` or `GetModuleFileName`) to read these appended bytes.

## 2. Reverse Engineering xorStub with Ghidra MCP
Ghidra disassembly of `xorStub.exe` highlights the simplicity and detection liability of this pattern:
1. `Assembly.GetEntryAssembly().Location` is invoked to read the on-disk file stream.
2. The byte stream is searched for the `***` marker.
3. The payload and key strings are split using the `|` delimiter.
4. The key is decrypted via `ROT13Encode(key, "randomkey")`.
5. The payload is written to `%TEMP%\<random>.exe`.
6. `Process.Start()` executes the dropped binary, followed by `File.Delete()` on exit.

## 3. Themida & Native Virtualization Stubs
In contrast to overlay droppers, commercial protectors (Themida, VMProtect) convert native x86 machine instructions into custom bytecode interpreted by an embedded virtual CPU:
- **Code Virtualization**: Eliminates standard x86 opcodes (`MOV`, `CALL`, `JMP`).
- **Polymorphic Mutation**: Scrambles opcode representations per compilation.
- **Hardware Breakpoint Clearing**: Injects thread context hooks modifying `DR0-DR3` registers.
- **Blue Team Detection**: While difficult to decompile statically, the VM interpreter loop creates distinctive execution entropy and CPU cycle timing anomalies detectable by modern EDR sensors.
