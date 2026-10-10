/*
  Rule: native_packer_antidebug_peb
  Description: Native Packer PEB BeingDebugged Inspection
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule native_packer_antidebug_peb
{
    meta:
        description = "Native Packer PEB BeingDebugged Inspection"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $peb1 = { 64 A1 30 00 00 00 0F B6 40 02 }
    $peb2 = { 65 48 8B 04 25 60 00 00 00 }

    condition:
        uint16(0) == 0x5A4D and (any of them)
}
