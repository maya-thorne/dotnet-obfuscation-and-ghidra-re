/*
  Rule: upx_compressed_pe_container
  Description: UPX Executable Compression Container
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule upx_compressed_pe_container
{
    meta:
        description = "UPX Executable Compression Container"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $u1 = "UPX0"
    $u2 = "UPX1"
    $u3 = "UPX!"

    condition:
        uint16(0) == 0x5A4D and (2 of them)
}
