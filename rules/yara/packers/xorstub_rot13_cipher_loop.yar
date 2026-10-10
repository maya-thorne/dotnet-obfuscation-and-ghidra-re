/*
  Rule: xorstub_rot13_cipher_loop
  Description: xorStub ROT13 / XOR Byte Transposition Engine
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule xorstub_rot13_cipher_loop
{
    meta:
        description = "xorStub ROT13 / XOR Byte Transposition Engine"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $x1 = "ROT13Encode"
    $x2 = { 02 03 8D ?? ?? ?? ?? 07 20 }

    condition:
        uint16(0) == 0x5A4D and (any of them)
}
