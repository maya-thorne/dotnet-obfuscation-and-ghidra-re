/*
  Rule: eazfuscator_net_virtual_machine
  Description: Eazfuscator.NET Bytecode Virtual Machine Dispatcher
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule eazfuscator_net_virtual_machine
{
    meta:
        description = "Eazfuscator.NET Bytecode Virtual Machine Dispatcher"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $ez1 = "Eazfuscator.NET"
    $ez2 = "Eazfuscator"
    $ez3 = { 20 ?? ?? ?? ?? 28 ?? ?? ?? ?? 02 28 }

    condition:
        uint16(0) == 0x5A4D and (2 of them)
}
