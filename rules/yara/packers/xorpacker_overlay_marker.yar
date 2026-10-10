/*
  Rule: xorpacker_overlay_marker
  Description: xorPacker Three-Star Overlay Token Marker
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule xorpacker_overlay_marker
{
    meta:
        description = "xorPacker Three-Star Overlay Token Marker"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $m1 = "***"
    $m2 = "randomkey"
    $m3 = "xorStub"

    condition:
        uint16(0) == 0x5A4D and (all of them)
}
