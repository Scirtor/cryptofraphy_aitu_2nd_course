"""
Unit tests for classical ciphers.

Run with: python -m pytest tests/
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from classical_ciphers.caesar_cipher import CaesarCipher
from classical_ciphers.vigenere_cipher import VigenereCipher


class TestCaesarCipher:
    """Test cases for Caesar cipher implementation."""
    
    def test_basic_encryption(self):
        """Test basic encryption with shift of 3."""
        cipher = CaesarCipher(shift=3)
        plaintext = "HELLO"
        expected = "KHOOR"
        assert cipher.encrypt(plaintext) == expected
    
    def test_basic_decryption(self):
        """Test basic decryption with shift of 3."""
        cipher = CaesarCipher(shift=3)
        ciphertext = "KHOOR"
        expected = "HELLO"
        assert cipher.decrypt(ciphertext) == expected
    
    def test_encryption_decryption_cycle(self):
        """Test that decrypt(encrypt(text)) == text."""
        cipher = CaesarCipher(shift=7)
        plaintext = "THE QUICK BROWN FOX"
        encrypted = cipher.encrypt(plaintext)
        decrypted = cipher.decrypt(encrypted)
        assert decrypted == plaintext
    
    def test_preserve_case(self):
        """Test that case is preserved."""
        cipher = CaesarCipher(shift=3)
        plaintext = "Hello World"
        encrypted = cipher.encrypt(plaintext)
        assert encrypted == "Khoor Zruog"
    
    def test_preserve_non_alpha(self):
        """Test that non-alphabetic characters are preserved."""
        cipher = CaesarCipher(shift=3)
        plaintext = "HELLO, WORLD! 123"
        encrypted = cipher.encrypt(plaintext)
        assert encrypted == "KHOOR, ZRUOG! 123"
    
    def test_shift_wrapping(self):
        """Test that shift wraps around the alphabet."""
        cipher = CaesarCipher(shift=1)
        assert cipher.encrypt("Z") == "A"
        assert cipher.encrypt("z") == "a"
    
    def test_rot13(self):
        """Test ROT13 (shift of 13)."""
        cipher = CaesarCipher(shift=13)
        plaintext = "HELLO"
        encrypted = cipher.encrypt(plaintext)
        # ROT13 is its own inverse
        assert cipher.encrypt(encrypted) == plaintext
    
    def test_zero_shift(self):
        """Test that shift of 0 returns unchanged text."""
        cipher = CaesarCipher(shift=0)
        plaintext = "HELLO WORLD"
        assert cipher.encrypt(plaintext) == plaintext
    
    def test_large_shift(self):
        """Test that large shifts are normalized."""
        cipher1 = CaesarCipher(shift=3)
        cipher2 = CaesarCipher(shift=29)  # 29 % 26 = 3
        plaintext = "HELLO"
        assert cipher1.encrypt(plaintext) == cipher2.encrypt(plaintext)
    
    def test_brute_force(self):
        """Test brute force attack returns all possibilities."""
        cipher = CaesarCipher()
        ciphertext = "KHOOR"
        results = cipher.brute_force(ciphertext)
        assert len(results) == 26
        # Check that one of the results is the correct plaintext
        plaintexts = [text for shift, text in results]
        assert "HELLO" in plaintexts


class TestVigenereCipher:
    """Test cases for Vigenère cipher implementation."""
    
    def test_basic_encryption(self):
        """Test basic encryption."""
        cipher = VigenereCipher("KEY")
        plaintext = "HELLO"
        expected = "RIJVS"
        assert cipher.encrypt(plaintext) == expected
    
    def test_basic_decryption(self):
        """Test basic decryption."""
        cipher = VigenereCipher("KEY")
        ciphertext = "RIJVS"
        expected = "HELLO"
        assert cipher.decrypt(ciphertext) == expected
    
    def test_encryption_decryption_cycle(self):
        """Test that decrypt(encrypt(text)) == text."""
        cipher = VigenereCipher("CRYPTO")
        plaintext = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
        encrypted = cipher.encrypt(plaintext)
        decrypted = cipher.decrypt(encrypted)
        assert decrypted == plaintext
    
    def test_preserve_case(self):
        """Test that case is preserved."""
        cipher = VigenereCipher("KEY")
        plaintext = "Hello World"
        encrypted = cipher.encrypt(plaintext)
        decrypted = cipher.decrypt(encrypted)
        assert decrypted == plaintext
    
    def test_preserve_non_alpha(self):
        """Test that non-alphabetic characters are preserved."""
        cipher = VigenereCipher("KEY")
        plaintext = "HELLO, WORLD! 123"
        encrypted = cipher.encrypt(plaintext)
        assert ", " in encrypted
        assert "!" in encrypted
        assert "123" in encrypted
    
    def test_key_repetition(self):
        """Test that key repeats correctly."""
        cipher = VigenereCipher("AB")
        # With key "AB", A shifts by 0, B shifts by 1, repeating A-B-A
        plaintext = "AAA"
        encrypted = cipher.encrypt(plaintext)
        assert encrypted == "ABA"  # A+A=A, A+B=B, A+A=A
    
    def test_single_char_key(self):
        """Test with single character key (equivalent to Caesar)."""
        key = "D"  # shift of 3
        cipher = VigenereCipher(key)
        plaintext = "HELLO"
        encrypted = cipher.encrypt(plaintext)
        # Should be same as Caesar with shift 3
        assert encrypted == "KHOOR"
    
    def test_invalid_key_raises_error(self):
        """Test that invalid keys raise ValueError."""
        with pytest.raises(ValueError):
            VigenereCipher("")
        
        with pytest.raises(ValueError):
            VigenereCipher("KEY123")
        
        with pytest.raises(ValueError):
            VigenereCipher("KEY WITH SPACES")
    
    def test_lowercase_key(self):
        """Test that lowercase keys work."""
        cipher1 = VigenereCipher("key")
        cipher2 = VigenereCipher("KEY")
        plaintext = "HELLO"
        assert cipher1.encrypt(plaintext) == cipher2.encrypt(plaintext)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
