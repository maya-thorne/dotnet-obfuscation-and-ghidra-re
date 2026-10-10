import unittest
from src.protector_heuristics import ProtectorHeuristics


class TestProtectorHeuristics(unittest.TestCase):

    def test_benign_binary(self):
        data = b"MZ" + (b"\x00" * 300)
        heuristics = ProtectorHeuristics(data)
        self.assertEqual(heuristics.confidence_verdict, "LOW (BENIGN / STANDARD COMPILATION)")
        self.assertEqual(len(heuristics.detected_protectors), 0)

    def test_confuserex_detection(self):
        data = b"MZ" + (b"\x00" * 200) + b"Confuser.Core" + b"\x00ConfusedByAttribute\x00" + b"VirtualProtect"
        heuristics = ProtectorHeuristics(data)
        protectors = [p["protector"] for p in heuristics.detected_protectors]
        self.assertIn("ConfuserEx", protectors)
        self.assertGreaterEqual(heuristics.risk_score, 50)

    def test_dotnet_reactor_detection(self):
        data = b"MZ" + (b"\x00" * 200) + b".reactor" + b"NecroBit" + b"NativeLoader"
        heuristics = ProtectorHeuristics(data)
        protectors = [p["protector"] for p in heuristics.detected_protectors]
        self.assertIn(".NET Reactor", protectors)
        self.assertGreaterEqual(heuristics.risk_score, 50)


if __name__ == "__main__":
    unittest.main()
