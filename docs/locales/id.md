<div align="center">

<p align="center">
  <a href="../../README.md">🇺🇸 English</a> · <a href="./ko.md">🇰🇷 한국어</a> · <a href="./zh-CN.md">🇨🇳 中文</a> · <a href="./es.md">🇪🇸 Español</a> · <a href="./hi.md">🇮🇳 हिन्दी</a><br />
  <a href="./ar.md">🇸🇦 العربية</a> · <a href="./pt-BR.md">🇧🇷 Português</a> · <a href="./ru.md">🇷🇺 Русский</a> · <a href="./fr.md">🇫🇷 Français</a> · <a href="./id.md">🇮🇩 Bahasa Indonesia</a>
</p>

<p align="center">
  <a href="https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"><img src="../assets/locales/id/banner.svg" alt="dotnet-obfuscation-and-ghidra-re banner" width="100%" /></a>
</p>

# 🛡️ dotnet-obfuscation-and-ghidra-re

**Rekayasa Deteksi Blue Team EDR/SIEM, 52 Aturan Sigma, 32 Aturan YARA, Forensik CIL & Suite Ghidra RE**

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

## 📌 Ringkasan Eksekutif

Assembly .NET dikompilasi menjadi bytecode CIL dan metadata CLI yang transparan. Penyerang menggunakan ConfuserEx, .NET Reactor, dan xorPacker untuk menghindari deteksi antivirus.

Repositori ini menyediakan **kerangka deteksi defensif tingkat perusahaan untuk analis SOC/EDR**, menggabungkan 52 aturan Sigma, 32 aturan YARA, dan mesin pembalik xorPacker.

---

## 🏛️ Arsitektur Sistem & Pipeline Forensik

<p align="center">
  <a href="https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"><img src="../assets/locales/id/architecture.svg" alt="architecture diagram" width="100%" /></a>
</p>

---

## 🏗️ Pipeline Deteksi EDR/SIEM

<p align="center">
  <a href="https://github.com/maya-thorne/dotnet-obfuscation-and-ghidra-re"><img src="../assets/locales/id/detection_pipeline.svg" alt="Detection Pipeline" width="100%" /></a>
</p>

---

## 💻 Demonstrasi Terminal

<p align="center">
  <img src="../assets/demo_dotnet_terminal.svg" alt="Terminal Demo" width="100%" />
</p>

---

## 📚 Indeks Whitepaper Riset

<table width="100%">
  <thead>
    <tr>
      <th width="32%">Dokumen Riset</th>
      <th width="68%">Cakupan Teknis dan Target Analisis</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        🔬 <strong><a href="../whitepapers/01_DOTNET_CIL_METADATA_AND_JIT_FORENSICS.md">01_DOTNET_CIL_METADATA_AND_JIT_FORENSICS.md</a></strong><br>
        <code>01_DOTNET_CIL_METADATA_AND_JIT_FORENSICS.md</code>
      </td>
      <td>
        Struktur ECMA-335 CLI, stream #Strings, #US, #Blob dan eksploitasi Invalid Metadata.
      </td>
    </tr>
    <tr>
      <td>
        🔬 <strong><a href="../whitepapers/02_CONFUSEREX_8_PHASE_EVASION_DECONSTRUCTION.md">02_CONFUSEREX_8_PHASE_EVASION_DECONSTRUCTION.md</a></strong><br>
        <code>02_CONFUSEREX_8_PHASE_EVASION_DECONSTRUCTION.md</code>
      </td>
      <td>
        Dekonstruksi hook AntiTamper JIT, AntiDump, dan flattening control flow.
      </td>
    </tr>
    <tr>
      <td>
        🔬 <strong><a href="../whitepapers/03_NATIVE_PACKER_PE_OVERLAY_AND_STUB_RE.md">03_NATIVE_PACKER_PE_OVERLAY_AND_STUB_RE.md</a></strong><br>
        <code>03_NATIVE_PACKER_PE_OVERLAY_AND_STUB_RE.md</code>
      </td>
      <td>
        Ekstraksi overlay PE, pembalikan XOR dua tahap, dan analisis stub Themida.
      </td>
    </tr>
    <tr>
      <td>
        🔬 <strong><a href="../whitepapers/04_COMMERCIAL_OBFUSCATOR_TAXONOMY_AND_HEURISTICS.md">04_COMMERCIAL_OBFUSCATOR_TAXONOMY_AND_HEURISTICS.md</a></strong><br>
        <code>04_COMMERCIAL_OBFUSCATOR_TAXONOMY_AND_HEURISTICS.md</code>
      </td>
      <td>
        Taksonomi dan tanda tangan untuk 8 pelindung komersial (.NET Reactor, Babel).
      </td>
    </tr>
  </tbody>
</table>

---

## 🛡️ Matriks Pertahanan MITRE ATT&CK

Full MITRE ATT&CK matrix: [docs/MITRE_ATTACK_DEFENSE_MATRIX.md](../MITRE_ATTACK_DEFENSE_MATRIX.md)
