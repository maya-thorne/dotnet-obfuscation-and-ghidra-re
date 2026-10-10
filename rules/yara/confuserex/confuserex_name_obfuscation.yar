/*
  Rule: confuserex_name_obfuscation
  Description: ConfuserEx Non-Printable Identifier Unicode Renamer
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule confuserex_name_obfuscation
{
    meta:
        description = "ConfuserEx Non-Printable Identifier Unicode Renamer"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $n1 = { E2 80 8B E2 80 8C E2 80 8D }
    $n2 = { EF BB BF }

    condition:
        uint16(0) == 0x5A4D and (any of them)
}
