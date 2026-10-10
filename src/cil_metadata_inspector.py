#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
🔬 .NET CIL Metadata Stream & Anomaly Inspector
===============================================================================
Author: Maya Thorne (Systems & Reverse Engineering Research)
License: MT-SRL (Maya Thorne Systems & Security Research License)

Inspects ECMA-335 CLI Metadata structures (#Strings, #US, #Blob, #GUID, #~).
Detects Invalid Metadata attacks, corrupted stream headers, and anti-decompilation
tricks deployed by ConfuserEx, .NET Reactor, and advanced obfuscators.
===============================================================================
"""

import struct
from typing import Dict, List, Any, Optional
from .pe_overlay_detector import PEOverlayDetector


class CILMetadataInspector:
    """Parses and audits .NET CLI headers and metadata streams."""

    def __init__(self, data: bytes, pe_info: Optional[PEOverlayDetector] = None):
        self.data = data
        self.size = len(data)
        self.pe_info = pe_info or PEOverlayDetector(data)
        self.is_dotnet = False
        self.runtime_version = ""
        self.metadata_rva = 0
        self.metadata_size = 0
        self.metadata_offset = 0
        self.streams: List[Dict[str, Any]] = []
        self.invalid_metadata_flags: List[str] = []
        self.has_invalid_metadata = False

        self._analyze()

    def _rva_to_offset(self, rva: int) -> Optional[int]:
        """Translates RVA to raw file offset using PE section headers."""
        for sec in self.pe_info.sections:
            va = sec["virtual_address"]
            vsize = sec["virtual_size"]
            raw_ptr = sec["raw_offset"]
            raw_size = sec["raw_size"]
            if va <= rva < va + max(vsize, raw_size):
                return raw_ptr + (rva - va)
        return None

    def _analyze(self):
        """Analyzes CLI Header and Metadata streams."""
        if not self.pe_info.is_valid_pe or self.pe_info.cli_header_rva == 0:
            return

        cli_offset = self._rva_to_offset(self.pe_info.cli_header_rva)
        if cli_offset is None or cli_offset + 72 > self.size:
            self.invalid_metadata_flags.append("CLI_HEADER_OUT_OF_BOUNDS")
            self.has_invalid_metadata = True
            return

        self.is_dotnet = True

        # Parse IMAGE_COR20_HEADER
        cb, major_rt, minor_rt, meta_rva, meta_size, flags, entry_point = struct.unpack_from(
            "<IIIIIII", self.data, cli_offset
        )
        self.metadata_rva = meta_rva
        self.metadata_size = meta_size

        if meta_rva == 0 or meta_size == 0:
            self.invalid_metadata_flags.append("NULL_METADATA_DIRECTORY")
            self.has_invalid_metadata = True
            return

        meta_offset = self._rva_to_offset(meta_rva)
        if meta_offset is None or meta_offset + 16 > self.size:
            self.invalid_metadata_flags.append("METADATA_ROOT_OUT_OF_BOUNDS")
            self.has_invalid_metadata = True
            return

        self.metadata_offset = meta_offset

        # Check BSJB Magic (0x424A5342)
        (magic,) = struct.unpack_from("<I", self.data, meta_offset)
        if magic != 0x424A5342:
            self.invalid_metadata_flags.append(f"CORRUPT_BSJB_MAGIC (0x{magic:08X})")
            self.has_invalid_metadata = True
            return

        # Read Version Length
        version_len_offset = meta_offset + 12
        if version_len_offset + 4 > self.size:
            return
        (version_len,) = struct.unpack_from("<I", self.data, version_len_offset)
        if version_len > 256 or version_len_offset + 4 + version_len > self.size:
            self.invalid_metadata_flags.append("ANOMALOUS_VERSION_LENGTH")
            self.has_invalid_metadata = True
            return

        raw_ver = self.data[version_len_offset + 4:version_len_offset + 4 + version_len]
        self.runtime_version = raw_ver.split(b"\x00")[0].decode("ascii", errors="ignore")

        # Stream Headers offset
        stream_count_offset = version_len_offset + 4 + version_len + 2
        if stream_count_offset + 2 > self.size:
            return
        (stream_count,) = struct.unpack_from("<H", self.data, stream_count_offset)

        curr_ptr = stream_count_offset + 2
        for _ in range(stream_count):
            if curr_ptr + 8 > self.size:
                self.invalid_metadata_flags.append("TRUNCATED_STREAM_HEADER")
                self.has_invalid_metadata = True
                break

            s_offset, s_size = struct.unpack_from("<II", self.data, curr_ptr)
            curr_ptr += 8

            name_bytes = bytearray()
            while curr_ptr < self.size:
                b = self.data[curr_ptr]
                curr_ptr += 1
                if b == 0:
                    break
                name_bytes.append(b)

            # Pad to 4-byte boundary
            curr_ptr = (curr_ptr + 3) & ~3
            stream_name = name_bytes.decode("ascii", errors="ignore")

            # Check bounds
            abs_stream_start = meta_offset + s_offset
            if abs_stream_start + s_size > self.size:
                self.invalid_metadata_flags.append(f"STREAM_OVERFLOW ({stream_name})")
                self.has_invalid_metadata = True

            self.streams.append({
                "name": stream_name,
                "relative_offset": s_offset,
                "size": s_size,
                "absolute_offset": abs_stream_start
            })

        # Check for standard stream anomalies
        stream_names = [s["name"] for s in self.streams]
        if "#~" not in stream_names and "#-" not in stream_names:
            self.invalid_metadata_flags.append("MISSING_TABLES_STREAM (#~ / #-)")
            self.has_invalid_metadata = True

        if "#Strings" not in stream_names:
            self.invalid_metadata_flags.append("MISSING_STRINGS_STREAM")
            self.has_invalid_metadata = True

    def to_dict(self) -> Dict[str, Any]:
        """Serializes CLI metadata inspection to dictionary."""
        return {
            "is_dotnet": self.is_dotnet,
            "runtime_version": self.runtime_version,
            "metadata_rva": hex(self.metadata_rva) if self.metadata_rva else None,
            "metadata_size": self.metadata_size,
            "metadata_offset": hex(self.metadata_offset) if self.metadata_offset else None,
            "streams_count": len(self.streams),
            "streams": self.streams,
            "has_invalid_metadata": self.has_invalid_metadata,
            "anomalies": self.invalid_metadata_flags
        }
