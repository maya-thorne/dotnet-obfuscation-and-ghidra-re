import unittest
import base64
from src.xor_packer_hunter import XorPackerHunter


class TestXorPackerHunter(unittest.TestCase):

    def test_rot13_xor_cipher_symmetry(self):
        msg = "ConfuserEx_AntiTamper_Payload_2026"
        key = "randomkey"
        encoded = XorPackerHunter.rot13_xor_cipher(msg, key)
        decoded = XorPackerHunter.rot13_xor_cipher(encoded, key)
        self.assertEqual(decoded, msg)

    def test_xor_packer_marker_carving(self):
        # Construct realistic xorPacker overlay
        master_key = "randomkey"
        dyn_key = "SessionKey_9999"
        target_payload = b"MZ\x90\x00\x03\x00\x00\x00DECRYPTED_TEST_PAYLOAD"

        # Encrypt dyn_key with master_key
        enc_key_str = XorPackerHunter.rot13_xor_cipher(dyn_key, master_key)
        b64_enc_key = base64.b64encode(enc_key_str.encode("utf-8")).decode("ascii")

        # Encrypt payload with dyn_key
        b64_pe = base64.b64encode(target_payload).decode("ascii")
        enc_payload_str = XorPackerHunter.rot13_xor_cipher(b64_pe, dyn_key)
        b64_ciphered_payload = base64.b64encode(enc_payload_str.encode("utf-8")).decode("ascii")

        overlay_text = f"***{b64_ciphered_payload}|{b64_enc_key}"

        dummy_binary = b"MZ" + (b"\x90" * 500) + overlay_text.encode("ascii")

        hunter = XorPackerHunter(dummy_binary)
        self.assertTrue(hunter.has_xor_packer_marker)
        self.assertEqual(hunter.recovered_random_key, dyn_key)
        self.assertTrue(hunter.is_payload_valid_pe)
        self.assertEqual(hunter.decrypted_payload, target_payload)


if __name__ == "__main__":
    unittest.main()
