/*
  Rule: confuserex_resource_encryption
  Description: ConfuserEx Encrypted Resource Stream Carve
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule confuserex_resource_encryption
{
    meta:
        description = "ConfuserEx Encrypted Resource Stream Carve"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $r1 = "System.Resources.ResourceReader"
    $r2 = { 72 ?? ?? ?? ?? 28 ?? ?? ?? ?? 6F }

    condition:
        uint16(0) == 0x5A4D and (all of them)
}
