import unittest
import struct
from src.pe_overlay_detector import PEOverlayDetector


class TestPEOverlayDetector(unittest.TestCase):

    def _create_minimal_pe(self, num_sections=1, raw_data_size=512, append_overlay=b""):
        """Constructs a structurally valid in-memory minimal PE32 binary."""
        e_lfanew = 0x80
        dos_header = bytearray(e_lfanew)
        dos_header[0:2] = b"MZ"
        struct.pack_into("<I", dos_header, 0x3C, e_lfanew)

        # File Header
        file_header = struct.pack("<4sHHIIIHH", b"PE\x00\x00", 0x14C, num_sections, 0, 0, 0, 0xE0, 0x102)

        # Optional Header (PE32)
        opt_header = bytearray(0xE0)
        struct.pack_into("<H", opt_header, 0, 0x10B)  # Magic 0x10B = PE32
        struct.pack_into("<I", opt_header, 16, 0x1000)  # AddressOfEntryPoint
        struct.pack_into("<I", opt_header, 28, 0x400000)  # ImageBase
        struct.pack_into("<I", opt_header, 32, 0x1000)  # SectionAlignment
        struct.pack_into("<I", opt_header, 36, 0x200)  # FileAlignment

        # Section Header (.text)
        sec_header = bytearray(40 * num_sections)
        raw_ptr = e_lfanew + len(file_header) + len(opt_header) + len(sec_header)
        # Align raw_ptr to FileAlignment
        raw_ptr = (raw_ptr + 0x1FF) & ~0x1FF

        struct.pack_into(
            "<8sIIIIIIHHI",
            sec_header,
            0,
            b".text\x00\x00\x00",
            0x1000,  # VirtualSize
            0x1000,  # VirtualAddress
            raw_data_size,  # SizeOfRawData
            raw_ptr,  # PointerToRawData
            0, 0, 0, 0,
            0x60000020  # Characteristics
        )

        pe_bytes = dos_header + file_header + opt_header + sec_header
        if len(pe_bytes) < raw_ptr:
            pe_bytes += b"\x00" * (raw_ptr - len(pe_bytes))

        # Add section raw body
        pe_bytes += b"\x90" * raw_data_size

        if append_overlay:
            pe_bytes += append_overlay

        return bytes(pe_bytes)

    def test_shannon_entropy(self):
        # Uniform zero entropy
        self.assertEqual(PEOverlayDetector.calculate_entropy(b"\x00" * 100), 0.0)
        # Random high entropy
        random_bytes = bytes([i % 256 for i in range(1024)])
        self.assertGreater(PEOverlayDetector.calculate_entropy(random_bytes), 7.8)

    def test_pe_parsing_without_overlay(self):
        pe_data = self._create_minimal_pe(num_sections=1, raw_data_size=512)
        detector = PEOverlayDetector(pe_data)

        self.assertTrue(detector.is_valid_pe)
        self.assertFalse(detector.is_64bit)
        self.assertEqual(detector.number_of_sections, 1)
        self.assertFalse(detector.has_overlay)
        self.assertEqual(detector.overlay_size, 0)

    def test_pe_parsing_with_overlay(self):
        overlay_payload = b"***EXTRACTED_CIPHER_OVERLAY_PAYLOAD***"
        pe_data = self._create_minimal_pe(num_sections=1, raw_data_size=512, append_overlay=overlay_payload)
        detector = PEOverlayDetector(pe_data)

        self.assertTrue(detector.is_valid_pe)
        self.assertTrue(detector.has_overlay)
        self.assertEqual(detector.overlay_size, len(overlay_payload))
        self.assertEqual(detector.overlay_bytes, overlay_payload)


if __name__ == "__main__":
    unittest.main()
