import unittest
import yes_please

class MyTestCase(unittest.TestCase):
    def test_encrypt_decript_string(self):
        s = "my test string"
        encrypted = yes_please.encrypt_string_to_string(s)
        decrypted = yes_please.decrypt_string_to_string(encrypted)
        self.assertEqual(s, decrypted)
    def test_encrypt_decript_string_none(self):
        s = ""
        encrypted = yes_please.encrypt_string_to_string(s)
        self.assertEqual(s, encrypted)
    def test_encrypt_decript_string_numb(self):
        s = "1234"
        encrypted = yes_please.encrypt_string_to_string(s)
        decrypted = yes_please.decrypt_string_to_string(encrypted)
        self.assertEqual(s, decrypted)

if __name__ == '__main__':
    unittest.main()
