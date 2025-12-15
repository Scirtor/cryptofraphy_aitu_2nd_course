"""
AES (Advanced Encryption Standard) Examples

AES is a symmetric encryption algorithm widely used across the globe.
It was established by the U.S. National Institute of Standards and Technology (NIST) in 2001.

This module demonstrates how to use the cryptography library for AES encryption.

Note: This uses a well-tested library (cryptography) rather than implementing AES from scratch,
which is the recommended approach for production use.

Author: AITU Cryptography Course
"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os


class AESCipher:
    """
    AES encryption/decryption wrapper using CBC mode with PKCS7 padding.
    
    Attributes:
        key (bytes): 256-bit encryption key
    """
    
    def __init__(self, key=None):
        """
        Initialize AES cipher with a key.
        
        Args:
            key (bytes): 32-byte key for AES-256. If None, generates a random key.
        """
        if key is None:
            # Generate a random 256-bit (32-byte) key
            self.key = os.urandom(32)
        else:
            if len(key) not in [16, 24, 32]:  # AES-128, AES-192, AES-256
                raise ValueError("Key must be 16, 24, or 32 bytes long")
            self.key = key
    
    def encrypt(self, plaintext):
        """
        Encrypt plaintext using AES-CBC mode.
        
        Args:
            plaintext (str or bytes): The text to encrypt
            
        Returns:
            tuple: (iv, ciphertext) where both are bytes
            
        Example:
            >>> cipher = AESCipher()
            >>> iv, ciphertext = cipher.encrypt("Secret message")
        """
        # Convert string to bytes if necessary
        if isinstance(plaintext, str):
            plaintext = plaintext.encode('utf-8')
        
        # Generate a random initialization vector (IV)
        iv = os.urandom(16)  # AES block size is 128 bits (16 bytes)
        
        # Create cipher object
        cipher = Cipher(
            algorithms.AES(self.key),
            modes.CBC(iv),
            backend=default_backend()
        )
        
        # Add PKCS7 padding
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plaintext) + padder.finalize()
        
        # Encrypt
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        
        return iv, ciphertext
    
    def decrypt(self, iv, ciphertext):
        """
        Decrypt ciphertext using AES-CBC mode.
        
        Args:
            iv (bytes): Initialization vector used during encryption
            ciphertext (bytes): The encrypted data
            
        Returns:
            str: The decrypted plaintext
            
        Example:
            >>> cipher = AESCipher(key)
            >>> plaintext = cipher.decrypt(iv, ciphertext)
        """
        # Create cipher object
        cipher = Cipher(
            algorithms.AES(self.key),
            modes.CBC(iv),
            backend=default_backend()
        )
        
        # Decrypt
        decryptor = cipher.decryptor()
        padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        
        # Remove PKCS7 padding
        unpadder = padding.PKCS7(128).unpadder()
        plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
        
        return plaintext.decode('utf-8')
    
    def get_key_hex(self):
        """
        Get the encryption key in hexadecimal format.
        
        Returns:
            str: Hexadecimal representation of the key
        """
        return self.key.hex()


def main():
    """
    Demonstration of AES encryption usage.
    """
    print("=" * 50)
    print("AES ENCRYPTION DEMONSTRATION")
    print("=" * 50)
    
    # Example 1: Basic encryption and decryption
    cipher = AESCipher()
    plaintext = "This is a secret message!"
    
    print(f"\nOriginal text: {plaintext}")
    print(f"Key (hex): {cipher.get_key_hex()}")
    
    iv, ciphertext = cipher.encrypt(plaintext)
    print(f"IV (hex): {iv.hex()}")
    print(f"Ciphertext (hex): {ciphertext.hex()}")
    
    decrypted = cipher.decrypt(iv, ciphertext)
    print(f"Decrypted text: {decrypted}")
    
    # Example 2: Using a specific key
    print("\n" + "=" * 50)
    print("USING A SPECIFIC KEY")
    print("=" * 50)
    
    # Create a 256-bit key (32 bytes)
    specific_key = b'This is a 32-byte key for AES!!'
    cipher2 = AESCipher(key=specific_key)
    plaintext2 = "Another secret message with a known key"
    
    print(f"\nOriginal text: {plaintext2}")
    print(f"Key: {specific_key.decode('utf-8')}")
    
    iv2, ciphertext2 = cipher2.encrypt(plaintext2)
    print(f"Ciphertext (hex): {ciphertext2.hex()[:50]}...")
    
    decrypted2 = cipher2.decrypt(iv2, ciphertext2)
    print(f"Decrypted text: {decrypted2}")
    
    # Example 3: Demonstrating that same plaintext produces different ciphertexts
    print("\n" + "=" * 50)
    print("DIFFERENT IVs PRODUCE DIFFERENT CIPHERTEXTS")
    print("=" * 50)
    
    plaintext3 = "Same message"
    print(f"\nPlaintext: {plaintext3}")
    
    iv3a, ciphertext3a = cipher2.encrypt(plaintext3)
    iv3b, ciphertext3b = cipher2.encrypt(plaintext3)
    
    print(f"First encryption (hex):  {ciphertext3a.hex()}")
    print(f"Second encryption (hex): {ciphertext3b.hex()}")
    print(f"Ciphertexts are different: {ciphertext3a != ciphertext3b}")
    print(f"But both decrypt correctly: {cipher2.decrypt(iv3a, ciphertext3a)}, {cipher2.decrypt(iv3b, ciphertext3b)}")


if __name__ == "__main__":
    main()
