/*
  Rule: generic_high_entropy_pe_overlay
  Description: Generic Suspicious PE Overlay Header
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule generic_high_entropy_pe_overlay
{
    meta:
        description = "Generic Suspicious PE Overlay Header"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $ov1 = { 4D 5A 90 00 }
    $ov2 = "This program cannot be run in DOS mode."

    condition:
        uint16(0) == 0x5A4D and (all of them)
}
