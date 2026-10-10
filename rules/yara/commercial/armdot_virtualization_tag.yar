/*
  Rule: armdot_virtualization_tag
  Description: ArmDot Protector Virtual Machine Marker
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule armdot_virtualization_tag
{
    meta:
        description = "ArmDot Protector Virtual Machine Marker"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $ar1 = "ArmDot"
    $ar2 = "ArmDotAttribute"
    $ar3 = "ArmDot.Client"

    condition:
        uint16(0) == 0x5A4D and (any of them)
}
