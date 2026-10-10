# 🔬 ConfuserEx 8-Phase Protection Source Deconstructions & References
Author: Maya Thorne (Systems & Reverse Engineering Research)
License: MT-SRL

## 1. AntiTamper Protection (`Confuser.Protections/AntiTamper`)
ConfuserEx AntiTamper works at the JIT compilation layer. It encrypts all CIL method bodies inside the PE file and installs a runtime hook using `VirtualProtect` to decrypt the method bytes immediately prior to execution.

```csharp
// Source: Confuser.Protections/AntiTamper/DynamicDeriver.cs
public class DynamicDeriver : IKeyDeriver {
    public void Init(ConfuserContext ctx, RandomGenerator random) { ... }
    public uint DeriveKey(uint[] state, uint key) {
        // Multi-round arithmetic key derivation
        for (int i = 0; i < state.Length; i++) {
            key = (key ^ state[i]) * 0x5a1a1a1a;
        }
        return key;
    }
}
```

## 2. AntiDump Protection (`Confuser.Protections/AntiDump`)
AntiDump clears the PE header fields and section headers in memory after process initialization, blinding tools like MegaDumper, Scylla, or Process Dump.

```csharp
// Source: Confuser.Runtime/AntiDump.cs
internal static unsafe void Initialize() {
    uint oldProtect;
    byte* baseAddr = (byte*)Marshal.GetHINSTANCE(typeof(AntiDump).Module);
    byte* pNtHeader = baseAddr + *(uint*)(baseAddr + 0x3c);
    ushort numSections = *(ushort*)(pNtHeader + 6);
    ushort optHeaderSize = *(ushort*)(pNtHeader + 0x14);
    byte* sectionHeaders = pNtHeader + 0x18 + optHeaderSize;

    // Erase PE Headers in memory
    VirtualProtect((IntPtr)baseAddr, 0x1000, 0x40, out oldProtect);
    for (int i = 0; i < 0x1000; i++) {
        baseAddr[i] = 0;
    }
}
```

## 3. AntiDebug Protection (`Confuser.Protections/AntiDebug`)
AntiDebug installs a background watchdog thread continuously polling `Debugger.IsAttached`, `CheckRemoteDebuggerPresent`, and PEB flags.

```csharp
// Source: Confuser.Runtime/AntiDebugAntinet.cs
internal static void Initialize() {
    Thread worker = new Thread(() => {
        while (true) {
            if (Debugger.IsAttached || Debugger.IsLogging()) {
                Environment.FailFast("Debugger detected");
            }
            Thread.Sleep(500);
        }
    });
    worker.IsBackground = true;
    worker.Start();
}
```
