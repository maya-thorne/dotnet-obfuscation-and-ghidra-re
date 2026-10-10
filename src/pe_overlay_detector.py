#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
🔬 PE Overlay & Structural Anomaly Detector
===============================================================================
Author: Maya Thorne (Systems & Reverse Engineering Research)
License: MT-SRL (Maya Thorne Systems & Security Research License)

Provides pure Python parsing of PE headers (PE32/PE32+), section table bounds,
PE overlay carving, and section-by-section Shannon entropy calculation.
===============================================================================
"""

import math
import struct
from typing import Dict, List, Any, Optional, Tuple


class PEOverlayDetector:
    """Detects and analyzes PE file structure, section bounds, and overlays."""

    def __init__(self, data: bytes):
        self.data = data
        self.size = len(data)
        self.is_valid_pe = False
        self.is_64bit = False
        self.nt_header_offset = 0
        self.number_of_sections = 0
        self.sections: List[Dict[str, Any]] = []
        self.expected_raw_size = 0
        self.has_overlay = False
        self.overlay_offset = 0
        self.overlay_size = 0
        self.overlay_bytes = b""
        self.overlay_entropy = 0.0
        self.cli_header_rva = 0
        self.cli_header_size = 0

        self._parse()

    @staticmethod
    def calculate_entropy(data: bytes) -> float:
        """Calculates Shannon entropy for the given byte array (0.0 to 8.0)."""
        if not data:
            return 0.0
        entropy = 0.0
        length = len(data)
        byte_counts = [0] * 256
        for b in data:
            byte_counts[b] += 1
        for count in byte_counts:
            if count > 0:
                p = count / length
                entropy -= p * math.log2(p)
        return round(entropy, 4)

    def _parse(self):
        """Parses DOS Header, PE Headers, and Section Headers."""
        if self.size < 64:
            return
        # Check DOS magic 'MZ'
        if self.data[:2] != b"MZ":
            return

        # Read e_lfanew
        (e_lfanew,) = struct.unpack_from("<I", self.data, 0x3C)
        if e_lfanew + 24 > self.size:
            return

        # Check PE signature 'PE\0\0'
        if self.data[e_lfanew:e_lfanew + 4] != b"PE\x00\x00":
            return

        self.nt_header_offset = e_lfanew
        self.is_valid_pe = True

        # File Header
        file_header_offset = e_lfanew + 4
        machine, num_sections, _, _, _, size_opt_header, characteristics = struct.unpack_from(
            "<HHIIIHH", self.data, file_header_offset
        )
        self.number_of_sections = num_sections

        # Optional Header
        opt_header_offset = file_header_offset + 20
        if opt_header_offset + 2 > self.size:
            return
        (magic,) = struct.unpack_from("<H", self.data, opt_header_offset)
        self.is_64bit = (magic == 0x20B)  # 0x10B = PE32, 0x20B = PE32+

        # Check for CLR Data Directory (Index 14)
        data_dirs_offset = opt_header_offset + (112 if self.is_64bit else 96)
        clr_dir_offset = data_dirs_offset + (14 * 8)
        if clr_dir_offset + 8 <= self.size and clr_dir_offset + 8 <= opt_header_offset + size_opt_header:
            clr_rva, clr_size = struct.unpack_from("<II", self.data, clr_dir_offset)
            self.cli_header_rva = clr_rva
            self.cli_header_size = clr_size

        # Parse Section Headers
        section_headers_offset = opt_header_offset + size_opt_header
        max_end_raw = section_headers_offset

        for i in range(num_sections):
            sec_offset = section_headers_offset + (i * 40)
            if sec_offset + 40 > self.size:
                break
            raw_name, virt_size, virt_addr, raw_size, raw_ptr, _, _, _, _, chars = struct.unpack_from(
                "<8sIIIIIIHHI", self.data, sec_offset
            )
            clean_name = raw_name.split(b"\x00")[0].decode("latin-1", errors="ignore")
            sec_end = raw_ptr + raw_size
            if sec_end > max_end_raw:
                max_end_raw = sec_end

            sec_data = self.data[raw_ptr:raw_ptr + raw_size] if raw_ptr + raw_size <= self.size else self.data[raw_ptr:]
            sec_entropy = self.calculate_entropy(sec_data)

            self.sections.append({
                "name": clean_name,
                "virtual_address": virt_addr,
                "virtual_size": virt_size,
                "raw_offset": raw_ptr,
                "raw_size": raw_size,
                "entropy": sec_entropy,
                "characteristics": chars
            })

        self.expected_raw_size = max_end_raw

        # Check for Overlay
        if self.size > self.expected_raw_size:
            self.has_overlay = True
            self.overlay_offset = self.expected_raw_size
            self.overlay_size = self.size - self.expected_raw_size
            self.overlay_bytes = self.data[self.overlay_offset:]
            self.overlay_entropy = self.calculate_entropy(self.overlay_bytes)

    def to_dict(self) -> Dict[str, Any]:
        """Serializes detection results to dictionary."""
        return {
            "is_valid_pe": self.is_valid_pe,
            "architecture": "x64 (PE32+)" if self.is_64bit else "x86 (PE32)",
            "number_of_sections": self.number_of_sections,
            "total_file_size": self.size,
            "expected_raw_size": self.expected_raw_size,
            "has_cli_header": self.cli_header_rva > 0,
            "cli_header_rva": hex(self.cli_header_rva) if self.cli_header_rva else None,
            "has_overlay": self.has_overlay,
            "overlay_offset": hex(self.overlay_offset) if self.has_overlay else None,
            "overlay_size": self.overlay_size,
            "overlay_entropy": self.overlay_entropy,
            "sections": self.sections
        }
