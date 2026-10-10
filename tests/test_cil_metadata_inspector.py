import unittest
from src.pe_overlay_detector import PEOverlayDetector
from src.cil_metadata_inspector import CILMetadataInspector


class TestCILMetadataInspector(unittest.TestCase):

    def test_non_pe_handling(self):
        inspector = CILMetadataInspector(b"RANDOM_NON_PE_DATA")
        self.assertFalse(inspector.is_dotnet)
        self.assertFalse(inspector.has_invalid_metadata)

    def test_pe_without_dotnet(self):
        # Plain PE without CLI Header
        pe_detector = PEOverlayDetector(b"MZ" + b"\x00" * 200)
        inspector = CILMetadataInspector(b"MZ" + b"\x00" * 200, pe_detector)
        self.assertFalse(inspector.is_dotnet)


if __name__ == "__main__":
    unittest.main()
