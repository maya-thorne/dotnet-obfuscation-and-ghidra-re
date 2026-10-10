/*
  Rule: pe_overlay_base64_blob
  Description: High-Density Base64 ASCII Stream in PE Overlay
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule pe_overlay_base64_blob
{
    meta:
        description = "High-Density Base64 ASCII Stream in PE Overlay"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $b64 = /TVqQAAMAAAAEAAAA\/\/\/\/[A-Za-z0-9+\/]{40,}/

    condition:
        uint16(0) == 0x5A4D and ($b64)
}
