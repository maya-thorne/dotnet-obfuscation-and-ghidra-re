/*
  Rule: themida_oreans_virtualization
  Description: Themida Oreans Code Virtualization Stub
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule themida_oreans_virtualization
{
    meta:
        description = "Themida Oreans Code Virtualization Stub"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $th1 = "Themida"
    $th2 = "Oreans Technologies"
    $th3 = ".themida"

    condition:
        uint16(0) == 0x5A4D and (any of them)
}
