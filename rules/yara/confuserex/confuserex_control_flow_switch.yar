/*
  Rule: confuserex_control_flow_switch
  Description: ConfuserEx Control Flow Flattening Switch Dispatcher
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule confuserex_control_flow_switch
{
    meta:
        description = "ConfuserEx Control Flow Flattening Switch Dispatcher"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $cf1 = { 45 ?? ?? ?? ?? 38 ?? ?? ?? ?? 28 }
    $cf2 = { 2B ?? ?? ?? ?? 38 }

    condition:
        uint16(0) == 0x5A4D and (any of them)
}
