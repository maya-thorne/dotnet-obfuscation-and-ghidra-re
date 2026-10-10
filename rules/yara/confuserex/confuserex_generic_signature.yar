/*
  Rule: confuserex_generic_signature
  Description: ConfuserEx General Binary Protection Marker
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule confuserex_generic_signature
{
    meta:
        description = "ConfuserEx General Binary Protection Marker"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $g1 = "ConfusedByAttribute"
    $g2 = "ConfuserEx v"
    $g3 = "yck1509"

    condition:
        uint16(0) == 0x5A4D and (any of them)
}
