/*
  Rule: babel_obfuscator_manifest
  Description: Babel .NET Assembly Obfuscation Manifest
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule babel_obfuscator_manifest
{
    meta:
        description = "Babel .NET Assembly Obfuscation Manifest"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $b1 = "BabelAttribute"
    $b2 = "BabelObfuscator"
    $b3 = "Babel .NET"

    condition:
        uint16(0) == 0x5A4D and (any of them)
}
