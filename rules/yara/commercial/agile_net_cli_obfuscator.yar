/*
  Rule: agile_net_cli_obfuscator
  Description: Agile.NET (CliSecure) Protector Signature
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule agile_net_cli_obfuscator
{
    meta:
        description = "Agile.NET (CliSecure) Protector Signature"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $ag1 = "CliSecure"
    $ag2 = "Agile.NET"

    condition:
        uint16(0) == 0x5A4D and (any of them)
}
