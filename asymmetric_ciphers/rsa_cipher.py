"""
RSA (Rivest-Shamir-Adleman) Cipher Implementation

RSA is one of the first public-key cryptosystems and is widely used for secure data transmission.
In RSA, the encryption key is public and differs from the decryption key which is kept secret (private).

This module demonstrates RSA encryption, decryption, and digital signatures.

Note: This uses the cryptography library for production-ready implementation.

Author: AITU Cryptography Course
"""

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend


class RSACipher:
    """
    RSA encryption/decryption and digital signature wrapper.
    
    Attributes:
        private_key: RSA private key
        public_key: RSA public key
    """
    
    def __init__(self, key_size=2048):
        """
        Initialize RSA cipher by generating a key pair.
        
        Args:
            key_size (int): Size of the RSA key in bits (default: 2048)
                           Common values: 1024, 2048, 4096
        """
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()
    
    def encrypt(self, plaintext):
        """
        Encrypt plaintext using the public key.
        
        Args:
            plaintext (str or bytes): The text to encrypt
            
        Returns:
            bytes: The encrypted ciphertext
            
        Note:
            Maximum message size is limited by key size and padding.
            For RSA-2048 with OAEP padding: ~190 bytes
            
        Example:
            >>> cipher = RSACipher()
            >>> ciphertext = cipher.encrypt("Secret message")
        """
        if isinstance(plaintext, str):
            plaintext = plaintext.encode('utf-8')
        
        ciphertext = self.public_key.encrypt(
            plaintext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext
    
    def decrypt(self, ciphertext, return_bytes=False):
        """
        Decrypt ciphertext using the private key.
        
        Args:
            ciphertext (bytes): The encrypted data
            return_bytes (bool): If True, return bytes instead of string
            
        Returns:
            str or bytes: The decrypted plaintext
            
        Example:
            >>> cipher = RSACipher()
            >>> plaintext = cipher.decrypt(ciphertext)
        """
        plaintext = self.private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        if return_bytes:
            return plaintext
        return plaintext.decode('utf-8')
    
    def sign(self, message):
        """
        Create a digital signature for a message using the private key.
        
        Args:
            message (str or bytes): The message to sign
            
        Returns:
            bytes: The digital signature
            
        Example:
            >>> cipher = RSACipher()
            >>> signature = cipher.sign("Important message")
        """
        if isinstance(message, str):
            message = message.encode('utf-8')
        
        signature = self.private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature
    
    def verify(self, message, signature):
        """
        Verify a digital signature using the public key.
        
        Args:
            message (str or bytes): The original message
            signature (bytes): The signature to verify
            
        Returns:
            bool: True if signature is valid, False otherwise
            
        Example:
            >>> cipher = RSACipher()
            >>> is_valid = cipher.verify("Important message", signature)
        """
        if isinstance(message, str):
            message = message.encode('utf-8')
        
        try:
            self.public_key.verify(
                signature,
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False
    
    def export_public_key_pem(self):
        """
        Export the public key in PEM format.
        
        Returns:
            str: PEM-encoded public key
        """
        pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return pem.decode('utf-8')
    
    def export_private_key_pem(self):
        """
        Export the private key in PEM format (without encryption).
        
        Returns:
            str: PEM-encoded private key
            
        Warning:
            Private keys should be protected! In production, use password encryption.
        """
        pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        return pem.decode('utf-8')


def main():
    """
    Demonstration of RSA encryption and digital signatures.
    """
    print("=" * 50)
    print("RSA ENCRYPTION DEMONSTRATION")
    print("=" * 50)
    
    # Example 1: Basic encryption and decryption
    cipher = RSACipher(key_size=2048)
    plaintext = "This is a secret message!"
    
    print(f"\nOriginal text: {plaintext}")
    
    ciphertext = cipher.encrypt(plaintext)
    print(f"Ciphertext (hex): {ciphertext.hex()[:50]}...")
    print(f"Ciphertext length: {len(ciphertext)} bytes")
    
    decrypted = cipher.decrypt(ciphertext)
    print(f"Decrypted text: {decrypted}")
    
    # Example 2: Digital signatures
    print("\n" + "=" * 50)
    print("DIGITAL SIGNATURE DEMONSTRATION")
    print("=" * 50)
    
    message = "This document is authentic and has not been tampered with."
    print(f"\nMessage: {message}")
    
    signature = cipher.sign(message)
    print(f"Signature (hex): {signature.hex()[:50]}...")
    print(f"Signature length: {len(signature)} bytes")
    
    # Verify the signature
    is_valid = cipher.verify(message, signature)
    print(f"\nSignature is valid: {is_valid}")
    
    # Try to verify with modified message
    tampered_message = "This document has been tampered with."
    is_valid_tampered = cipher.verify(tampered_message, signature)
    print(f"Signature is valid for tampered message: {is_valid_tampered}")
    
    # Example 3: Key export
    print("\n" + "=" * 50)
    print("KEY EXPORT DEMONSTRATION")
    print("=" * 50)
    
    public_key_pem = cipher.export_public_key_pem()
    print("\nPublic Key (PEM format):")
    print(public_key_pem[:100] + "...")
    
    print("\nPrivate Key (first 100 chars):")
    private_key_pem = cipher.export_private_key_pem()
    print(private_key_pem[:100] + "...")
    print("\n⚠️  Never share your private key!")


if __name__ == "__main__":
    main()
