/*
  Rule: dotnet_reactor_native_loader
  Description: .NET Reactor Native Wrapper Loader Thunk
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule dotnet_reactor_native_loader
{
    meta:
        description = ".NET Reactor Native Wrapper Loader Thunk"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $nl1 = "NativeLoader"
    $nl2 = "Eziriz .NET Reactor"

    condition:
        uint16(0) == 0x5A4D and (any of them)
}
