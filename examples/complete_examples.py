"""
Complete Cryptography Examples

This file demonstrates how to use all the cipher implementations together
in practical scenarios.

Author: AITU Cryptography Course
"""

import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classical_ciphers.caesar_cipher import CaesarCipher
from classical_ciphers.vigenere_cipher import VigenereCipher


def classical_cipher_example():
    """
    Demonstrate classical cipher usage.
    """
    print("=" * 60)
    print("CLASSICAL CIPHERS EXAMPLE")
    print("=" * 60)
    
    message = "MEET ME AT THE PARK AT MIDNIGHT"
    print(f"\nOriginal message: {message}")
    
    # Caesar cipher
    print("\n--- Caesar Cipher (shift=7) ---")
    caesar = CaesarCipher(shift=7)
    caesar_encrypted = caesar.encrypt(message)
    print(f"Encrypted: {caesar_encrypted}")
    print(f"Decrypted: {caesar.decrypt(caesar_encrypted)}")
    
    # Vigenère cipher
    print("\n--- Vigenère Cipher (key=SECRET) ---")
    vigenere = VigenereCipher("SECRET")
    vigenere_encrypted = vigenere.encrypt(message)
    print(f"Encrypted: {vigenere_encrypted}")
    print(f"Decrypted: {vigenere.decrypt(vigenere_encrypted)}")


def hybrid_encryption_example():
    """
    Demonstrate hybrid encryption (combining symmetric and asymmetric).
    
    This is how real-world systems like TLS/SSL work:
    1. Use RSA to securely exchange an AES key
    2. Use AES to encrypt the actual data (faster for large data)
    """
    print("\n" + "=" * 60)
    print("HYBRID ENCRYPTION EXAMPLE (RSA + AES)")
    print("=" * 60)
    
    try:
        from symmetric_ciphers.aes_example import AESCipher
        from asymmetric_ciphers.rsa_cipher import RSACipher
        
        # Scenario: Alice wants to send a large message to Bob
        print("\nScenario: Alice sends encrypted message to Bob")
        print("-" * 60)
        
        # Bob generates RSA key pair
        print("\n1. Bob generates RSA key pair (public and private)")
        bob_rsa = RSACipher(key_size=2048)
        
        # Alice gets Bob's public key
        print("2. Alice receives Bob's public key")
        
        # Alice generates AES key for this session
        print("3. Alice generates random AES session key")
        alice_aes = AESCipher()
        
        # Alice encrypts the AES key with Bob's RSA public key
        print("4. Alice encrypts AES key using Bob's RSA public key")
        encrypted_aes_key = bob_rsa.encrypt(alice_aes.key)
        
        # Alice encrypts her message with AES
        large_message = "This is a confidential message that could be very long. " * 10
        print(f"5. Alice encrypts message with AES")
        print(f"   Message length: {len(large_message)} characters")
        iv, encrypted_message = alice_aes.encrypt(large_message)
        
        # Alice sends: encrypted_aes_key, iv, encrypted_message
        print("6. Alice sends: (encrypted_aes_key, iv, encrypted_message)")
        
        # Bob decrypts the AES key with his RSA private key
        print("\n7. Bob decrypts AES key using his RSA private key")
        decrypted_aes_key = bob_rsa.decrypt(encrypted_aes_key, return_bytes=True)
        
        # Bob creates AES cipher with the decrypted key
        print("8. Bob creates AES cipher with decrypted key")
        bob_aes = AESCipher(key=decrypted_aes_key)
        
        # Bob decrypts the message
        print("9. Bob decrypts the message with AES")
        decrypted_message = bob_aes.decrypt(iv, encrypted_message)
        
        print(f"\n✓ Decrypted message (first 100 chars): {decrypted_message[:100]}...")
        print(f"✓ Successful: {decrypted_message == large_message}")
        
    except ImportError as e:
        print(f"\nNote: Install 'cryptography' package to run this example")
        print(f"Run: pip install cryptography")


def password_hashing_example():
    """
    Demonstrate proper password hashing.
    """
    print("\n" + "=" * 60)
    print("PASSWORD HASHING EXAMPLE")
    print("=" * 60)
    
    try:
        from hash_functions.sha_example import HashFunctions
        
        password = "MySecurePassword123!"
        print(f"\nOriginal password: {password}")
        
        # Bad practice: plain MD5 (shown for educational purposes)
        print("\n⚠️  BAD: Plain MD5 hash (easily crackable)")
        md5_hash = HashFunctions.md5(password)
        print(f"MD5: {md5_hash}")
        
        # Better: SHA-256 (still not ideal for passwords)
        print("\n⚠️  BETTER: SHA-256 (but still not ideal for passwords)")
        sha256_hash = HashFunctions.sha256(password)
        print(f"SHA-256: {sha256_hash}")
        
        # Best practice would use bcrypt/scrypt/argon2 (not implemented here)
        print("\n✓  BEST: Use bcrypt, scrypt, or Argon2 in production!")
        print("   These are specifically designed for password hashing")
        
        # Demonstrate salt usage
        print("\n" + "-" * 60)
        print("IMPORTANCE OF SALT")
        print("-" * 60)
        
        import os
        salt1 = os.urandom(16).hex()
        salt2 = os.urandom(16).hex()
        
        salted_hash1 = HashFunctions.sha256(password + salt1)
        salted_hash2 = HashFunctions.sha256(password + salt2)
        
        print(f"\nSame password with different salts:")
        print(f"Hash 1: {salted_hash1}")
        print(f"Hash 2: {salted_hash2}")
        print(f"Hashes are different: {salted_hash1 != salted_hash2}")
        
    except ImportError:
        print("\nNote: Some hash functions require standard library only")


def digital_signature_example():
    """
    Demonstrate digital signatures for document verification.
    """
    print("\n" + "=" * 60)
    print("DIGITAL SIGNATURE EXAMPLE")
    print("=" * 60)
    
    try:
        from asymmetric_ciphers.rsa_cipher import RSACipher
        
        # Scenario: Alice signs a document
        print("\nScenario: Alice signs a contract, Bob verifies it")
        print("-" * 60)
        
        alice_rsa = RSACipher()
        
        contract = "I, Alice, agree to the terms and conditions of this contract."
        print(f"\nContract: {contract}")
        
        # Alice signs the contract
        print("\n1. Alice signs the contract with her private key")
        signature = alice_rsa.sign(contract)
        print(f"   Signature (first 50 chars): {signature.hex()[:50]}...")
        
        # Bob verifies the signature with Alice's public key
        print("2. Bob verifies signature with Alice's public key")
        is_valid = alice_rsa.verify(contract, signature)
        print(f"   Signature is valid: {is_valid}")
        
        # Someone tries to modify the contract
        print("\n3. Mallory tries to modify the contract")
        modified_contract = "I, Alice, agree to give Mallory all my money."
        print(f"   Modified: {modified_contract}")
        
        # Verification fails for modified contract
        print("4. Bob verifies modified contract with same signature")
        is_valid_modified = alice_rsa.verify(modified_contract, signature)
        print(f"   Signature is valid: {is_valid_modified}")
        print(f"   ✓ Tampering detected!")
        
    except ImportError as e:
        print(f"\nNote: Install 'cryptography' package to run this example")


def main():
    """
    Run all examples.
    """
    print("\n" + "=" * 60)
    print("COMPREHENSIVE CRYPTOGRAPHY EXAMPLES")
    print("=" * 60)
    
    classical_cipher_example()
    hybrid_encryption_example()
    password_hashing_example()
    digital_signature_example()
    
    print("\n" + "=" * 60)
    print("ALL EXAMPLES COMPLETED")
    print("=" * 60)
    print("\n⚠️  Remember: These are educational implementations.")
    print("Always use well-tested cryptographic libraries in production!")


if __name__ == "__main__":
    main()
