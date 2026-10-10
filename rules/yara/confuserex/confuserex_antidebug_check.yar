/*
  Rule: confuserex_antidebug_check
  Description: ConfuserEx AntiDebug Debugger.IsAttached Poll
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule confuserex_antidebug_check
{
    meta:
        description = "ConfuserEx AntiDebug Debugger.IsAttached Poll"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $d1 = "Debugger.IsAttached"
    $d2 = "CheckRemoteDebuggerPresent"
    $d3 = "IsDebuggerPresent"

    condition:
        uint16(0) == 0x5A4D and (any of them)
}
