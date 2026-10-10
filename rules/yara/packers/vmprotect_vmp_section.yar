/*
  Rule: vmprotect_vmp_section
  Description: VMProtect Hypervisor Stub Section Header
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule vmprotect_vmp_section
{
    meta:
        description = "VMProtect Hypervisor Stub Section Header"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $v1 = ".vmp0"
    $v2 = ".vmp1"
    $v3 = "VMProtect"

    condition:
        uint16(0) == 0x5A4D and (any of them)
}
