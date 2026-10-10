/*
  Rule: intellilock_trial_licensing
  Description: IntelliLock Licensing and Expiration Hook
  Author: Maya Thorne (Systems & Reverse Engineering Research)
  License: MT-SRL
  Date: 2026-10-11
*/

rule intellilock_trial_licensing
{
    meta:
        description = "IntelliLock Licensing and Expiration Hook"
        author = "Maya Thorne"
        license = "MT-SRL"
        reference = "https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"
        version = "1.0.0"

    strings:
    $il1 = "IntelliLock"
    $il2 = "IntelliLockTrial"
    $il3 = "IntelliLock.Licensing"

    condition:
        uint16(0) == 0x5A4D and (any of them)
}
