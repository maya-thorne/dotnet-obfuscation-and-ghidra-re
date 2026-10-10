#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
🔬 dotnet-obfuscation-and-ghidra-re CLI Forensic Analysis Utility
===============================================================================
Author: Maya Thorne (Systems & Reverse Engineering Research)
License: MT-SRL (Maya Thorne Systems & Security Research License)

Command-line interface for analyzing PE binaries, inspecting .NET CIL metadata,
carving overlays, and extracting payloads.
===============================================================================
"""

import sys
import os
import json
import argparse
from typing import Optional

from .pe_overlay_detector import PEOverlayDetector
from .cil_metadata_inspector import CILMetadataInspector
from .xor_packer_hunter import XorPackerHunter
from .protector_heuristics import ProtectorHeuristics


def print_banner():
    print(r"""
===============================================================================
  🔬 dotnet-obfuscation-and-ghidra-re · Blue Team Forensic Analyzer
===============================================================================
  Engineered by Maya Thorne · Systems & Reverse Engineering Research
===============================================================================
""")


def analyze_file(filepath: str, verbose: bool = False, extract_overlay: Optional[str] = None, unpack_payload: Optional[str] = None) -> dict:
    if not os.path.isfile(filepath):
        print(f"[!] Error: File '{filepath}' not found.")
        sys.exit(1)

    with open(filepath, "rb") as f:
        data = f.read()

    heuristics = ProtectorHeuristics(data)
    report = heuristics.to_dict()

    print(f"[*] Target Binary: {filepath} ({len(data):,} bytes)")
    print(f"[*] Architecture:  {report['pe_summary']['architecture']}")
    print(f"[*] Is .NET Assembly: {report['cil_summary']['is_dotnet']}")
    if report['cil_summary']['is_dotnet']:
        print(f"[*] CLR Runtime:   {report['cil_summary']['runtime_version']}")
    print(f"[*] Risk Score:    {report['risk_score']} / 100")
    print(f"[*] Final Verdict: {report['verdict']}")

    print("\n--- Detected Protectors & Signatures ---")
    if report["detected_protectors"]:
        for p in report["detected_protectors"]:
            print(f"  [+] {p['protector']} (Confidence: {p['confidence']}) - Tokens: {', '.join(p['matched_tokens'])}")
    else:
        print("  [-] No standard signature matches detected.")

    print("\n--- Structural Telemetry & Indicators ---")
    for ind in report["indicators"]:
        print(f"  [!] {ind}")

    # Handle Overlay Extraction
    if extract_overlay and heuristics.pe_info.has_overlay:
        with open(extract_overlay, "wb") as f_out:
            f_out.write(heuristics.pe_info.overlay_bytes)
        print(f"\n[+] Carved PE Overlay ({heuristics.pe_info.overlay_size:,} bytes) -> {extract_overlay}")

    # Handle Payload Unpacking
    if unpack_payload:
        if heuristics.xor_hunter.decrypted_payload:
            with open(unpack_payload, "wb") as f_out:
                f_out.write(heuristics.xor_hunter.decrypted_payload)
            print(f"\n[+] Unpacked Decrypted Payload ({len(heuristics.xor_hunter.decrypted_payload):,} bytes) -> {unpack_payload}")
        else:
            print("\n[-] Unpack failed: No valid decrypted payload could be extracted.")

    if verbose:
        print("\n--- Section Table Entropy Breakdown ---")
        for sec in report["pe_summary"]["sections"]:
            print(f"  Section: {sec['name']:<10} RawSize: {sec['raw_size']:<8} Entropy: {sec['entropy']:.4f}")

    return report


def main():
    parser = argparse.ArgumentParser(
        description="dotnet-obfuscation-and-ghidra-re CLI Forensic Analysis Tool"
    )
    parser.add_argument("target", help="Path to target executable (.exe / .dll)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Display verbose section telemetry")
    parser.add_argument("--json", help="Export analysis report as JSON")
    parser.add_argument("--extract-overlay", help="Carve raw PE overlay to specified output file")
    parser.add_argument("--unpack-payload", help="Extract decrypted payload to specified output file")

    args = parser.parse_args()

    print_banner()
    report = analyze_file(
        args.target,
        verbose=args.verbose,
        extract_overlay=args.extract_overlay,
        unpack_payload=args.unpack_payload
    )

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f_json:
            json.dump(report, f_json, indent=2)
        print(f"\n[+] JSON report written to: {args.json}")


if __name__ == "__main__":
    main()
