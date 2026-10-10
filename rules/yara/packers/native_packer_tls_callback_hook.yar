/*
  Rule: native_packer_tls_callback_hook
  Description: Pre-Execution TLS Callback Stub Injection
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule native_packer_tls_callback_hook
{
    meta:
        description = "Pre-Execution TLS Callback Stub Injection"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $tls = { 55 8B EC 56 8B 75 0C 85 F6 75 }

    condition:
        uint16(0) == 0x5A4D and ($tls)
}
