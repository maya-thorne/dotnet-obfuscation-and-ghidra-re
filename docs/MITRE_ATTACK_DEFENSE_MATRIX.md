# 🛡️ MITRE ATT&CK Enterprise Defense & Detection Matrix
Author: Maya Thorne (Systems & Detection Engineering Research)
License: MT-SRL

## 📊 Enterprise Coverage Matrix (30:70 Proportions)

<table width="100%">
  <thead>
    <tr>
      <th width="32%">MITRE ATT&CK Technique</th>
      <th width="68%">Detection Engineering & Defense Rule Mappings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        🏷️ <strong>T1027: Obfuscated Files</strong><br>
        <code>T1027.002: Software Packing</code>
      </td>
      <td>
        <strong>Detection Telemetry:</strong> Sigma rules <br>
        <code>proc_<wbr>creation_<wbr>win_<wbr>temp_<wbr>dropper_<wbr>exec.yml</code>, <br>
        <code>proc_<wbr>creation_<wbr>win_<wbr>dotnet_<wbr>pe_<wbr>overlay.yml</code>.<br>
        <strong>Static Signatures:</strong> YARA rules <br>
        <code>xorpacker_<wbr>overlay_<wbr>marker.yar</code>, <br>
        <code>upx_<wbr>compressed_<wbr>pe_<wbr>container.yar</code>.<br>
        <strong>Heuristic:</strong> Shannon entropy threshold (> 7.2) across PE sections and carved overlays.
      </td>
    </tr>
    <tr>
      <td>
        🏷️ <strong>T1055: Process Injection</strong><br>
        <code>T1055.002: Portable Executable Injection</code>
      </td>
      <td>
        <strong>Detection Telemetry:</strong> Sysmon EID 10 / EID 1.<br>
        Sigma <code>proc_<wbr>creation_<wbr>win_<wbr>xorstub_<wbr>parent_<wbr>child.yml</code>, <br>
        <code>proc_<wbr>creation_<wbr>win_<wbr>virtualprotect_<wbr>abuse.yml</code>.<br>
        <strong>Signature:</strong> YARA <code>confuserex_<wbr>antidump_<wbr>hook.yar</code>.
      </td>
    </tr>
    <tr>
      <td>
        🏷️ <strong>T1497: Virtualization / Sandbox Evasion</strong><br>
        <code>T1497.001: System Checks</code>
      </td>
      <td>
        <strong>Detection Telemetry:</strong> Sigma rules <br>
        <code>proc_<wbr>creation_<wbr>win_<wbr>debugger_<wbr>isattached_<wbr>poll.yml</code>, <br>
        <code>proc_<wbr>creation_<wbr>win_<wbr>checkremotedebuggerpresent.yml</code>, <br>
        <code>proc_<wbr>creation_<wbr>win_<wbr>wmi_<wbr>anti_<wbr>vm_<wbr>query.yml</code>.<br>
        <strong>Signature:</strong> YARA <code>confuserex_<wbr>antidebug_<wbr>check.yar</code>.
      </td>
    </tr>
    <tr>
      <td>
        🏷️ <strong>T1036: Masquerading</strong><br>
        <code>T1036.005: Match Legitimate Name or Location</code>
      </td>
      <td>
        <strong>Detection Telemetry:</strong> Sigma rules <br>
        <code>proc_<wbr>creation_<wbr>win_<wbr>hidden_<wbr>window_<wbr>pe.yml</code>, <br>
        <code>file_<wbr>create_<wbr>win_<wbr>temp_<wbr>random_<wbr>exe.yml</code>.<br>
        <strong>Telemetry:</strong> Parent process spawning CLI with <code>ShowWindow(hWnd, 0)</code> or hidden style flags.
      </td>
    </tr>
    <tr>
      <td>
        🏷️ <strong>T1070: Indicator Removal</strong><br>
        <code>T1070.004: File Deletion</code>
      </td>
      <td>
        <strong>Detection Telemetry:</strong> Sigma rule <br>
        <code>proc_<wbr>creation_<wbr>win_<wbr>self_<wbr>deleting_<wbr>temp.yml</code>.<br>
        <strong>Heuristic:</strong> Dropped binary triggering immediate self-deletion upon child process exit.
      </td>
    </tr>
    <tr>
      <td>
        🏷️ <strong>T1574: Hijack Execution Flow</strong><br>
        <code>T1574.010: COR_PROFILER</code>
      </td>
      <td>
        <strong>Detection Telemetry:</strong> Sigma rules <br>
        <code>proc_<wbr>creation_<wbr>win_<wbr>clr_<wbr>profiler_<wbr>injection.yml</code>, <br>
        <code>proc_<wbr>creation_<wbr>win_<wbr>cor_<wbr>profiler_<wbr>dll_<wbr>load.yml</code>.<br>
        <strong>Heuristic:</strong> Monitoring <code>COR_ENABLE_PROFILING</code> and <code>COR_PROFILER</code> GUID hijacking.
      </td>
    </tr>
  </tbody>
</table>
