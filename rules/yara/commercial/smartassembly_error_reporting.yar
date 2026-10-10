/*
  Rule: smartassembly_error_reporting
  Description: SmartAssembly Metadata Obfuscation Signature
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule smartassembly_error_reporting
{
    meta:
        description = "SmartAssembly Metadata Obfuscation Signature"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $sa1 = "SmartAssembly.Attributes.PoweredByAttribute"
    $sa2 = "Powered by SmartAssembly"

    condition:
        uint16(0) == 0x5A4D and (any of them)
}
