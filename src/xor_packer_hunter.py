#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
🔬 xorPacker & Two-Stage XOR Cipher Hunter & Unpacker
===============================================================================
Author: Maya Thorne (Systems & Reverse Engineering Research)
License: MT-SRL (Maya Thorne Systems & Security Research License)

Forensic heuristic analyzer and dual-stage XOR reverser targeting xorPacker
and xorStub dropper binaries. Extracts dynamic keys and restores payload.
===============================================================================
"""

import base64
from typing import Dict, Any, Optional, Tuple


class XorPackerHunter:
    """Specialized hunter and decryptor for xorPacker / xorStub variants."""

    MASTER_KEY = "randomkey"
    DELIMITER_MARKER = b"***"

    def __init__(self, data: bytes):
        self.data = data
        self.has_xor_packer_marker = False
        self.marker_offset = -1
        self.raw_settings = ""
        self.b64_ciphered_payload = ""
        self.b64_enc_key = ""
        self.recovered_random_key = ""
        self.decrypted_payload: Optional[bytes] = None
        self.is_payload_valid_pe = False

        self._scan()

    @staticmethod
    def rot13_xor_cipher(data: str, key: str) -> str:
        """Implements the xorStub custom ROT13Encode XOR loop algorithm."""
        data_len = len(data)
        key_len = len(key)
        if key_len == 0:
            return data
        output = []
        for i in range(data_len):
            output.append(chr(ord(data[i]) ^ ord(key[i % key_len])))
        return "".join(output)

    def _scan(self):
        """Scans binary data for xorPacker overlay markers and decrypts payload."""
        idx = self.data.find(self.DELIMITER_MARKER)
        if idx == -1:
            return

        self.has_xor_packer_marker = True
        self.marker_offset = idx

        # Extract text following marker
        try:
            raw_chunk = self.data[idx + len(self.DELIMITER_MARKER):]
            settings_str = raw_chunk.decode("ascii", errors="ignore").strip()
            self.raw_settings = settings_str

            if "|" not in settings_str:
                return

            parts = settings_str.split("|", 1)
            self.b64_ciphered_payload = parts[0].strip()
            self.b64_enc_key = parts[1].strip()

            # Step 1: Decode Base64 encrypted key and decrypt with master key
            key_bytes = base64.b64decode(self.b64_enc_key)
            enc_key_str = key_bytes.decode("utf-8", errors="ignore")
            self.recovered_random_key = self.rot13_xor_cipher(enc_key_str, self.MASTER_KEY)

            # Step 2: Decode Base64 cipheredFile, decrypt with recovered random key, decode Base64 PE
            ciphered_bytes = base64.b64decode(self.b64_ciphered_payload)
            ciphered_str = ciphered_bytes.decode("utf-8", errors="ignore")
            intermediate_b64 = self.rot13_xor_cipher(ciphered_str, self.recovered_random_key)
            pe_bytes = base64.b64decode(intermediate_b64)

            if pe_bytes[:2] == b"MZ":
                self.decrypted_payload = pe_bytes
                self.is_payload_valid_pe = True

        except Exception:
            pass

    def to_dict(self) -> Dict[str, Any]:
        """Serializes xorPacker hunter results to dictionary."""
        return {
            "has_xor_packer_marker": self.has_xor_packer_marker,
            "marker_offset": hex(self.marker_offset) if self.marker_offset != -1 else None,
            "recovered_random_key": self.recovered_random_key if self.recovered_random_key else None,
            "has_decrypted_payload": self.decrypted_payload is not None,
            "decrypted_payload_size": len(self.decrypted_payload) if self.decrypted_payload else 0,
            "is_payload_valid_pe": self.is_payload_valid_pe
        }
