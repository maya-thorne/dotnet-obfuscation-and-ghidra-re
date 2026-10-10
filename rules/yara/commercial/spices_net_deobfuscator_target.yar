/*
  Rule: spices_net_deobfuscator_target
  Description: Spices.Net Obfuscator Tag Signature
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule spices_net_deobfuscator_target
{
    meta:
        description = "Spices.Net Obfuscator Tag Signature"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $sp1 = "Spices.Net"
    $sp2 = "NineRays.Obfuscator"

    condition:
        uint16(0) == 0x5A4D and (any of them)
}
