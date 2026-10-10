/*
  Rule: confuserex_ref_proxy_thunk
  Description: ConfuserEx Reference Proxy Invoke Thunk
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule confuserex_ref_proxy_thunk
{
    meta:
        description = "ConfuserEx Reference Proxy Invoke Thunk"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $p1 = "System.Reflection.Emit.DynamicMethod"
    $p2 = { 73 ?? ?? ?? ?? 2A }

    condition:
        uint16(0) == 0x5A4D and (all of them)
}
