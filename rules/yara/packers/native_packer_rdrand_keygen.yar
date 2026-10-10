/*
  Rule: native_packer_rdrand_keygen
  Description: Hardware RDRAND Entropy Seed Generator
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule native_packer_rdrand_keygen
{
    meta:
        description = "Hardware RDRAND Entropy Seed Generator"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $rd1 = { 0F C7 F0 }
    $rd2 = { 0F C7 F1 }

    condition:
        uint16(0) == 0x5A4D and (any of them)
}
