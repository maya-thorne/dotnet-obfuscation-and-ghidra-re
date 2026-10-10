# 🔬 Commercial .NET Obfuscator Taxonomy & Heuristic Signatures
Author: Maya Thorne (Systems & Reverse Engineering Research)
License: MT-SRL

## 1. Comparative Analysis of 8 Enterprise Obfuscation Toolchains

<table width="100%">
  <thead>
    <tr>
      <th width="32%">Toolchain & Vendor</th>
      <th width="68%">Primary Defense Mechanism & Heuristic Signatures</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        🛡️ <strong>ConfuserEx</strong><br>
        <code>Open Source (yck1509)</code>
      </td>
      <td>
        <strong>Mechanism:</strong> dnlib-based CIL rewriter with JIT AntiTamper hooks.<br>
        <strong>Signatures:</strong> <code>ConfusedByAttribute</code>, non-printable UTF-8 renamer tokens, corrupted `#~` metadata masks.
      </td>
    </tr>
    <tr>
      <td>
        🛡️ <strong>.NET Reactor</strong><br>
        <code>Eziriz</code>
      </td>
      <td>
        <strong>Mechanism:</strong> NecroBit dynamic method decryptor and native PE wrapper.<br>
        <strong>Signatures:</strong> <code>.reactor</code> section name, <code>NativeLoader</code>, <code>Eziriz</code> string tokens.
      </td>
    </tr>
    <tr>
      <td>
        🛡️ <strong>Eazfuscator.NET</strong><br>
        <code>Gapotchenko</code>
      </td>
      <td>
        <strong>Mechanism:</strong> Instruction-level virtualization and homomorphic string encryption.<br>
        <strong>Signatures:</strong> Virtual machine dispatcher loops, <code>Eazfuscator.NET</code> metadata attributes.
      </td>
    </tr>
    <tr>
      <td>
        🛡️ <strong>Babel Obfuscator</strong><br>
        <code>Babelfor.NET</code>
      </td>
      <td>
        <strong>Mechanism:</strong> Advanced control flow flattening, XML reflection obfuscation.<br>
        <strong>Signatures:</strong> <code>BabelAttribute</code>, encrypted resource stream tables.
      </td>
    </tr>
    <tr>
      <td>
        🛡️ <strong>ArmDot</strong><br>
        <code>ArmDot Software</code>
      </td>
      <td>
        <strong>Mechanism:</strong> CIL-to-virtual-machine translation and dynamic obfuscation.<br>
        <strong>Signatures:</strong> <code>ArmDotAttribute</code>, embedded bytecode interpreters.
      </td>
    </tr>
    <tr>
      <td>
        🛡️ <strong>IntelliLock</strong><br>
        <code>Eziriz</code>
      </td>
      <td>
        <strong>Mechanism:</strong> Software licensing enforcement combined with assembly locking.<br>
        <strong>Signatures:</strong> <code>IntelliLockTrial</code>, trial expiration and hardware lock hooks.
      </td>
    </tr>
    <tr>
      <td>
        🛡️ <strong>DeepSea</strong><br>
        <code>DeepSea Software</code>
      </td>
      <td>
        <strong>Mechanism:</strong> High-performance control flow transformation.<br>
        <strong>Signatures:</strong> <code>DeepSeaObfuscator</code> assembly attributes.
      </td>
    </tr>
    <tr>
      <td>
        🛡️ <strong>xorPacker</strong><br>
        <code>Native Injector</code>
      </td>
      <td>
        <strong>Mechanism:</strong> Overlay dropper with dual-stage XOR cipher.<br>
        <strong>Signatures:</strong> <code>***</code> delimiter, <code>xorStub</code> tokens, high-entropy PE overlays.
      </td>
    </tr>
  </tbody>
</table>
