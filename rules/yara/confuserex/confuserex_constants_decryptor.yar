/*
  Rule: confuserex_constants_decryptor
  Description: ConfuserEx Dynamic Constants Decryption Helper
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule confuserex_constants_decryptor
{
    meta:
        description = "ConfuserEx Dynamic Constants Decryption Helper"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $c1 = { FE 0C ?? ?? 28 ?? ?? ?? ?? 2A }
    $c2 = "System.Reflection.Assembly"

    condition:
        uint16(0) == 0x5A4D and (all of them)
}
