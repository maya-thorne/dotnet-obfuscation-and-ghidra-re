/*
  Rule: dotnet_reactor_necrobit_engine
  Description: .NET Reactor NecroBit CIL Decryptor
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule dotnet_reactor_necrobit_engine
{
    meta:
        description = ".NET Reactor NecroBit CIL Decryptor"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $nr1 = ".reactor"
    $nr2 = "NecroBit"
    $nr3 = "Eziriz"

    condition:
        uint16(0) == 0x5A4D and (2 of them)
}
