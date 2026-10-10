/*
  Rule: deepsea_obfuscator_signature
  Description: DeepSea Obfuscator Watermark and Signature
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule deepsea_obfuscator_signature
{
    meta:
        description = "DeepSea Obfuscator Watermark and Signature"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $ds1 = "DeepSeaObfuscator"
    $ds2 = "DeepSea"

    condition:
        uint16(0) == 0x5A4D and (any of them)
}
