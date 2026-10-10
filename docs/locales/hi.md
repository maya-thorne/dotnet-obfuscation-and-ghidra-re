<div align="center">

<p align="center">
  <a href="../../README.md">🇺🇸 English</a> · <a href="./ko.md">🇰🇷 한국어</a> · <a href="./zh-CN.md">🇨🇳 中文</a> · <a href="./es.md">🇪🇸 Español</a> · <a href="./hi.md">🇮🇳 हिन्दी</a><br />
  <a href="./ar.md">🇸🇦 العربية</a> · <a href="./pt-BR.md">🇧🇷 Português</a> · <a href="./ru.md">🇷🇺 Русский</a> · <a href="./fr.md">🇫🇷 Français</a> · <a href="./id.md">🇮🇩 Bahasa Indonesia</a>
</p>

<p align="center">
  <a href="https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"><img src="../assets/locales/hi/banner.svg" alt="dotnet-obfuscation-and-ghidra-re banner" width="100%" /></a>
</p>

# 🛡️ dotnet-obfuscation-and-ghidra-re

**ब्लू टीम EDR/SIEM डिटेक्शन इंजीनियरिंग, 52 सिग्मा नियम, 32 यारा हस्ताक्षर और Ghidra रिवर्स इंजीनियरिंग सूट**

[![Release](https://img.shields.io/github/v/release/maya-thorne/dotnet-obfuscation-and-ghidra-re?color=10b981)](https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re/releases/latest)
[![Sigma Rules](https://img.shields.io/badge/Sigma_Rules-52_Modular-f59e0b.svg)](../../rules/sigma)
[![YARA Rules](https://img.shields.io/badge/YARA_Rules-32_Signatures-10b981.svg)](../../rules/yara)
[![SIEM Feeds](https://img.shields.io/badge/SIEM-Splunk_%26_Elastic-38bdf8.svg)](../../rules/siem_queries)
[![MITRE ATT&CK](https://img.shields.io/badge/MITRE_ATT%26CK-Enterprise_Matrix-818cf8.svg)](../MITRE_ATTACK_DEFENSE_MATRIX.md)
[![Tests](https://img.shields.io/badge/Tests-100%25_Passing-10b981.svg)](../../tests)
[![License: MT-SRL](https://img.shields.io/badge/License-MT--SRL-blue.svg)](../../LICENSE)

<sub>Engineered &amp; Audited by **[Maya Thorne](https://github.com/maya-thorne)** · Systems &amp; Reverse Engineering Research</sub>

</div>

---

## 📌 कार्यकारी अवलोकन

.NET असेंबली CIL और मेटाडेटा में संकलित होती हैं। हमलावर सुरक्षा से बचने के लिए ConfuserEx, .NET Reactor और xorPacker जैसे टूल्स का उपयोग करते हैं।

यह रिपोजिटरी **SOC और EDR विश्लेषकों के लिए एक व्यापक रक्षात्मक रूपरेखा** प्रदान करती है, जिसमें 52 सिग्मा नियम और 32 यारा हस्ताक्षर शामिल हैं।

---

## 🏛️ सिस्टम आर्किटेक्चर और फोरेंसिक पाइपलाइन

<p align="center">
  <a href="https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"><img src="../assets/locales/hi/architecture.svg" alt="architecture diagram" width="100%" /></a>
</p>

---

## 🏗️ EDR/SIEM डिटेक्शन पाइपलाइन

<p align="center">
  <a href="https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"><img src="../assets/locales/hi/detection_pipeline.svg" alt="Detection Pipeline" width="100%" /></a>
</p>

---

## 💻 टर्मिनल प्रदर्शन

<p align="center">
  <img src="../assets/demo_dotnet_terminal.svg" alt="Terminal Demo" width="100%" />
</p>

---

## 📚 अनुसंधान श्वेतपत्र अनुक्रमणिका

<table width="100%">
  <thead>
    <tr>
      <th width="32%">श्वेतपत्र दस्तावेज</th>
      <th width="68%">तकनीकी दायरा और विश्लेषण लक्ष्य</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        🔬 <strong><a href="../whitepapers/01_DOTNET_CIL_METADATA_AND_JIT_FORENSICS.md">01_DOTNET_CIL_METADATA_AND_JIT_FORENSICS.md</a></strong><br>
        <code>01_DOTNET_CIL_METADATA_AND_JIT_FORENSICS.md</code>
      </td>
      <td>
        ECMA-335 CIL संरचनाएं, #Strings, #US स्ट्रीम और इनवैलिड मेटाडेटा विश्लेषण।
      </td>
    </tr>
    <tr>
      <td>
        🔬 <strong><a href="../whitepapers/02_CONFUSEREX_8_PHASE_EVASION_DECONSTRUCTION.md">02_CONFUSEREX_8_PHASE_EVASION_DECONSTRUCTION.md</a></strong><br>
        <code>02_CONFUSEREX_8_PHASE_EVASION_DECONSTRUCTION.md</code>
      </td>
      <td>
        ConfuserEx AntiTamper JIT हुक्स, AntiDump और कंट्रोल फ्लो डिस्टॉर्शन।
      </td>
    </tr>
    <tr>
      <td>
        🔬 <strong><a href="../whitepapers/03_NATIVE_PACKER_PE_OVERLAY_AND_STUB_RE.md">03_NATIVE_PACKER_PE_OVERLAY_AND_STUB_RE.md</a></strong><br>
        <code>03_NATIVE_PACKER_PE_OVERLAY_AND_STUB_RE.md</code>
      </td>
      <td>
        xorPacker ओवरले निष्कर्षण, XOR डिक्रिप्शन और Themida स्टब विश्लेषण।
      </td>
    </tr>
    <tr>
      <td>
        🔬 <strong><a href="../whitepapers/04_COMMERCIAL_OBFUSCATOR_TAXONOMY_AND_HEURISTICS.md">04_COMMERCIAL_OBFUSCATOR_TAXONOMY_AND_HEURISTICS.md</a></strong><br>
        <code>04_COMMERCIAL_OBFUSCATOR_TAXONOMY_AND_HEURISTICS.md</code>
      </td>
      <td>
        8 प्रमुख प्रोटेक्टर्स (.NET Reactor, Babel, Eazfuscator) के हस्ताक्षर।
      </td>
    </tr>
  </tbody>
</table>

---

## 🛡️ MITRE ATT&CK रक्षा मैट्रिक्स

Full MITRE ATT&CK matrix: [docs/MITRE_ATTACK_DEFENSE_MATRIX.md](../MITRE_ATTACK_DEFENSE_MATRIX.md)
