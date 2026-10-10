/*
  Rule: confuserex_antitamper_loader
  Description: ConfuserEx AntiTamper JIT Hook Runtime Loader
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule confuserex_antitamper_loader
{
    meta:
        description = "ConfuserEx AntiTamper JIT Hook Runtime Loader"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $s1 = { 8D ?? ?? ?? ?? ?? E8 ?? ?? ?? ?? 8B ?? ?? 85 ?? 74 ?? }
    $t1 = "Confuser.Core"
    $t2 = "VirtualProtect"

    condition:
        uint16(0) == 0x5A4D and (all of ($t*) or $s1)
}
