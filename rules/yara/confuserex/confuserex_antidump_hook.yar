/*
  Rule: confuserex_antidump_hook
  Description: ConfuserEx AntiDump VirtualProtect Hook
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule confuserex_antidump_hook
{
    meta:
        description = "ConfuserEx AntiDump VirtualProtect Hook"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $a1 = "VirtualProtect"
    $a2 = { 6A 40 68 00 10 00 00 }
    $a3 = "ConfusedByAttribute"

    condition:
        uint16(0) == 0x5A4D and (2 of them)
}
