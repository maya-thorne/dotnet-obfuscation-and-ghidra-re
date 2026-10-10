/*
  Rule: xorstub_temp_dropper_path
  Description: xorStub Temp Dropper Path Reconstruction Tokens
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule xorstub_temp_dropper_path
{
    meta:
        description = "xorStub Temp Dropper Path Reconstruction Tokens"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $p1 = "AAAQSDQSDF"
    $p2 = "QSDQSFFF"
    $p3 = "JHJLHJKYTUTYU"

    condition:
        uint16(0) == 0x5A4D and (2 of them)
}
