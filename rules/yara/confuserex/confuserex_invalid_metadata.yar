/*
  Rule: confuserex_invalid_metadata
  Description: ConfuserEx Invalid Metadata Table Header Tamper
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule confuserex_invalid_metadata
{
    meta:
        description = "ConfuserEx Invalid Metadata Table Header Tamper"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $md1 = "BSJB"
    $md2 = { 00 00 00 00 00 00 00 00 23 7E }
    $md3 = { 23 53 74 72 69 6E 67 73 00 }

    condition:
        uint16(0) == 0x5A4D and (2 of them)
}
