#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
🔬 Multi-Protector & Obfuscator Heuristic Classifier
===============================================================================
Author: Maya Thorne (Systems & Reverse Engineering Research)
License: MT-SRL (Maya Thorne Systems & Security Research License)

Comprehensive heuristic classification engine identifying ConfuserEx,
.NET Reactor, Eazfuscator, Babel, ArmDot, IntelliLock, DeepSea,
xorPacker, and Themida/VMProtect native virtualization stubs.
===============================================================================
"""

from typing import Dict, List, Any, Optional
from .pe_overlay_detector import PEOverlayDetector
from .cil_metadata_inspector import CILMetadataInspector
from .xor_packer_hunter import XorPackerHunter


class ProtectorHeuristics:
    """Classifies binary protections and calculates evasion risk scores."""

    PROTECTOR_SIGNATURES = {
        "ConfuserEx": [
            b"Confuser.Core",
            b"ConfuserEx",
            b"Confuser v",
            b"\x00ConfusedByAttribute\x00",
            b"VirtualProtect",  # AntiDump
            b"Debugger.IsAttached",  # AntiDebug
        ],
        ".NET Reactor": [
            b".reactor",
            b"Eziriz",
            b"NecroBit",
            b"NativeLoader",
        ],
        "Eazfuscator.NET": [
            b"Eazfuscator.NET",
            b"Eazfuscator",
        ],
        "Babel Obfuscator": [
            b"BabelAttribute",
            b"BabelObfuscator",
            b"Babel .NET",
        ],
        "ArmDot": [
            b"ArmDot",
            b"ArmDotAttribute",
        ],
        "IntelliLock": [
            b"IntelliLock",
            b"IntelliLockTrial",
        ],
        "DeepSea": [
            b"DeepSeaObfuscator",
            b"DeepSea",
        ],
        "xorPacker": [
            b"xorStub",
            b"xorPacker",
            b"ROT13Encode",
            b"***"
        ],
        "Themida / Oreans": [
            b"Themida",
            b"Oreans Technologies",
            b".themida",
            b".oreans"
        ],
        "VMProtect": [
            b".vmp0",
            b".vmp1",
            b"VMProtect",
        ],
        "UPX": [
            b"UPX0",
            b"UPX1",
            b"UPX2",
            b"UPX!"
        ]
    }

    def __init__(self, data: bytes):
        self.data = data
        self.pe_info = PEOverlayDetector(data)
        self.cil_info = CILMetadataInspector(data, self.pe_info)
        self.xor_hunter = XorPackerHunter(data)

        self.detected_protectors: List[Dict[str, Any]] = []
        self.risk_score: int = 0
        self.confidence_verdict: str = "BENIGN"
        self.indicators: List[str] = []

        self._classify()

    def _classify(self):
        """Runs multi-pass classification heuristics."""
        # 1. Signature Matching
        for name, sigs in self.PROTECTOR_SIGNATURES.items():
            matched_sigs = []
            for sig in sigs:
                if sig in self.data:
                    matched_sigs.append(sig.decode("latin-1", errors="ignore"))

            if matched_sigs:
                weight = len(matched_sigs) * 20
                self.risk_score += weight
                self.detected_protectors.append({
                    "protector": name,
                    "confidence": "HIGH" if len(matched_sigs) >= 2 else "MEDIUM",
                    "matched_tokens": matched_sigs
                })
                self.indicators.append(f"PROTECTOR_SIGNATURE_MATCH: {name} ({', '.join(matched_sigs)})")

        # 2. Section Name & Entropy Heuristics
        for sec in self.pe_info.sections:
            sec_name = sec["name"]
            sec_entropy = sec["entropy"]

            # High entropy section (> 7.2) indicates encrypted or compressed payload
            if sec_entropy >= 7.2:
                self.risk_score += 15
                self.indicators.append(f"HIGH_ENTROPY_SECTION: {sec_name} (Entropy={sec_entropy:.2f})")

            # Check known packer section names
            if sec_name in [".reactor", ".themida", ".vmp0", ".vmp1", "UPX0", "UPX1"]:
                self.risk_score += 25
                self.indicators.append(f"PACKER_SECTION_NAME: {sec_name}")

        # 3. PE Overlay Heuristic
        if self.pe_info.has_overlay:
            self.risk_score += 20
            self.indicators.append(
                f"PE_OVERLAY_DETECTED: {self.pe_info.overlay_size} bytes (Entropy={self.pe_info.overlay_entropy:.2f})"
            )
            if self.pe_info.overlay_entropy >= 7.0:
                self.risk_score += 15
                self.indicators.append("HIGH_ENTROPY_OVERLAY_ENCRYPTED_PAYLOAD")

        # 4. xorPacker Direct Detection
        if self.xor_hunter.has_xor_packer_marker:
            self.risk_score += 35
            self.indicators.append("XOR_PACKER_MARKER_CONFIRMED")
            if self.xor_hunter.is_payload_valid_pe:
                self.risk_score += 40
                self.indicators.append("XOR_PACKER_DECRYPTED_PE_PAYLOAD_VERIFIED")

        # 5. Invalid Metadata Heuristics
        if self.cil_info.has_invalid_metadata:
            self.risk_score += 30
            for anom in self.cil_info.invalid_metadata_flags:
                self.indicators.append(f"CIL_METADATA_ANOMALY: {anom}")

        # Final Verdict
        if self.risk_score >= 80:
            self.confidence_verdict = "CRITICAL (MALICIOUS / PACKED)"
        elif self.risk_score >= 50:
            self.confidence_verdict = "HIGH (OBFUSCATED / SUSPICIOUS)"
        elif self.risk_score >= 25:
            self.confidence_verdict = "MEDIUM (ELEVATED ANOMALY)"
        else:
            self.confidence_verdict = "LOW (BENIGN / STANDARD COMPILATION)"

    def to_dict(self) -> Dict[str, Any]:
        """Serializes classification report to dictionary."""
        return {
            "verdict": self.confidence_verdict,
            "risk_score": self.risk_score,
            "detected_protectors": self.detected_protectors,
            "indicators": self.indicators,
            "pe_summary": self.pe_info.to_dict(),
            "cil_summary": self.cil_info.to_dict(),
            "xor_packer_summary": self.xor_hunter.to_dict()
        }
