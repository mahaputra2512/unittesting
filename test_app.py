import unittest
from app import shift_character, encrypt_text, decrypt_text, sanitize_text

class TestEncryptionApp(unittest.TestCase):

    def test_shift_character(self):
        result = shift_character('A', 3)
        print("\nTest 1.1: Shift 'A' by 3")
        print(f"Expected: 'D', Actual: '{result}' — {'PASS' if result == 'D' else 'FAIL'}")
        self.assertEqual(result, 'D')
        
        result = shift_character('a', 1)
        print("\nTest 1.2: Shift 'a' by 1")
        print(f"Expected: 'b', Actual: '{result}' — {'PASS' if result == 'b' else 'FAIL'}")
        self.assertEqual(result, 'b')
        
        result = shift_character('Z', 1)
        print("\nTest 1.3: Shift 'Z' by 1 (wrap-around)")
        print(f"Expected: 'A', Actual: '{result}' — {'PASS' if result == 'A' else 'FAIL'}")
        self.assertEqual(result, 'A')
        
        result = shift_character(' ', 3)
        print("\nTest 1.4: Shift ' ' (space) by 3 (non-alphabet character)")
        print(f"Expected: ' ', Actual: '{result}' — {'PASS' if result == ' ' else 'FAIL'}")
        self.assertEqual(result, ' ')

    def test_encrypt_text(self):
        result = encrypt_text("ABC", 3)
        print("\nTest 2.1: Encrypt 'ABC' with shift 3")
        print(f"Expected: 'DEF', Actual: '{result}' — {'PASS' if result == 'DEF' else 'FAIL'}")
        self.assertEqual(result, "DEF")
        
        result = encrypt_text("xyz", 2)
        print("\nTest 2.2: Encrypt 'xyz' with shift 2")
        print(f"Expected: 'zab', Actual: '{result}' — {'PASS' if result == 'zab' else 'FAIL'}")
        self.assertEqual(result, "zab")

    def test_decrypt_text(self):
        encrypted = encrypt_text("Hello", 5)
        result = decrypt_text(encrypted, 5)
        print("\nTest 3.1: Decrypt encrypted 'Hello' with shift 5")
        print(f"Expected: 'Hello', Actual: '{result}' — {'PASS' if result == 'Hello' else 'FAIL'}")
        self.assertEqual(result, "Hello")

    def test_sanitize_text(self):
        result = sanitize_text("Hello, World!")
        print("\nTest 4.1: Sanitize 'Hello, World!' (removing special characters)")
        print(f"Expected: 'Hello World', Actual: '{result}' — {'PASS' if result == 'Hello World' else 'FAIL'}")
        self.assertEqual(result, "Hello World")
        
        result = sanitize_text("1234 5678")
        print("\nTest 4.2: Sanitize '1234 5678' (numerical characters allowed)")
        print(f"Expected: '1234 5678', Actual: '{result}' — {'PASS' if result == '1234 5678' else 'FAIL'}")
        self.assertEqual(result, "1234 5678")

if __name__ == "__main__":
    unittest.main()
