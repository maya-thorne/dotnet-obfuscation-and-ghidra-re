/*
  Rule: generic_packer_oep_tail_jump
  Description: Original Entry Point (OEP) Assembly Tail Jump
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule generic_packer_oep_tail_jump
{
    meta:
        description = "Original Entry Point (OEP) Assembly Tail Jump"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $tj = { 61 E9 ?? ?? ?? ?? }

    condition:
        uint16(0) == 0x5A4D and ($tj)
}
