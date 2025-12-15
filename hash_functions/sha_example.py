"""
Cryptographic Hash Functions Examples

Hash functions are mathematical algorithms that map data of arbitrary size to a bit string
of a fixed size (a hash). They are designed to be one-way functions, meaning it should be
infeasible to invert them.

Common uses:
- Data integrity verification
- Password storage
- Digital signatures
- Message authentication codes (MACs)

This module demonstrates SHA-256, SHA-512, and other hash functions.

Author: AITU Cryptography Course
"""

import hashlib
import hmac


class HashFunctions:
    """
    Wrapper class for various cryptographic hash functions.
    """
    
    @staticmethod
    def sha256(data):
        """
        Compute SHA-256 hash of data.
        
        Args:
            data (str or bytes): Data to hash
            
        Returns:
            str: Hexadecimal digest of the hash
            
        Example:
            >>> HashFunctions.sha256("Hello World")
            'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e'
        """
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        hash_obj = hashlib.sha256(data)
        return hash_obj.hexdigest()
    
    @staticmethod
    def sha512(data):
        """
        Compute SHA-512 hash of data.
        
        Args:
            data (str or bytes): Data to hash
            
        Returns:
            str: Hexadecimal digest of the hash
        """
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        hash_obj = hashlib.sha512(data)
        return hash_obj.hexdigest()
    
    @staticmethod
    def sha1(data):
        """
        Compute SHA-1 hash of data.
        
        Note: SHA-1 is considered cryptographically broken and should not be used
        for security purposes. Use SHA-256 or SHA-512 instead.
        
        Args:
            data (str or bytes): Data to hash
            
        Returns:
            str: Hexadecimal digest of the hash
        """
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        hash_obj = hashlib.sha1(data)
        return hash_obj.hexdigest()
    
    @staticmethod
    def md5(data):
        """
        Compute MD5 hash of data.
        
        Note: MD5 is cryptographically broken and should not be used for security.
        It's included here for educational purposes only.
        
        Args:
            data (str or bytes): Data to hash
            
        Returns:
            str: Hexadecimal digest of the hash
        """
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        hash_obj = hashlib.md5(data)
        return hash_obj.hexdigest()
    
    @staticmethod
    def hmac_sha256(data, key):
        """
        Compute HMAC-SHA256 (Hash-based Message Authentication Code).
        
        HMAC provides both data integrity and authentication.
        
        Args:
            data (str or bytes): Data to authenticate
            key (str or bytes): Secret key for HMAC
            
        Returns:
            str: Hexadecimal digest of the HMAC
            
        Example:
            >>> HashFunctions.hmac_sha256("message", "secret_key")
        """
        if isinstance(data, str):
            data = data.encode('utf-8')
        if isinstance(key, str):
            key = key.encode('utf-8')
        
        hmac_obj = hmac.new(key, data, hashlib.sha256)
        return hmac_obj.hexdigest()
    
    @staticmethod
    def hash_file(filepath, algorithm='sha256'):
        """
        Compute hash of a file's contents.
        
        Args:
            filepath (str): Path to the file
            algorithm (str): Hash algorithm to use ('sha256', 'sha512', 'md5')
            
        Returns:
            str: Hexadecimal digest of the file hash
            
        Example:
            >>> HashFunctions.hash_file('document.pdf', 'sha256')
        """
        hash_obj = hashlib.new(algorithm)
        
        try:
            with open(filepath, 'rb') as f:
                # Read file in chunks to handle large files
                for chunk in iter(lambda: f.read(4096), b''):
                    hash_obj.update(chunk)
            return hash_obj.hexdigest()
        except FileNotFoundError:
            return f"Error: File '{filepath}' not found"
    
    @staticmethod
    def verify_integrity(data, expected_hash, algorithm='sha256'):
        """
        Verify data integrity by comparing hash with expected value.
        
        Args:
            data (str or bytes): Data to verify
            expected_hash (str): Expected hash value (hexadecimal)
            algorithm (str): Hash algorithm used
            
        Returns:
            bool: True if hashes match, False otherwise
            
        Example:
            >>> data = "Important message"
            >>> hash_val = HashFunctions.sha256(data)
            >>> HashFunctions.verify_integrity(data, hash_val)
            True
        """
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        hash_obj = hashlib.new(algorithm)
        hash_obj.update(data)
        computed_hash = hash_obj.hexdigest()
        
        return computed_hash == expected_hash


def main():
    """
    Demonstration of cryptographic hash functions.
    """
    print("=" * 50)
    print("CRYPTOGRAPHIC HASH FUNCTIONS DEMONSTRATION")
    print("=" * 50)
    
    # Example 1: Basic hashing
    message = "Hello, Cryptography!"
    
    print(f"\nOriginal message: {message}")
    print(f"SHA-256: {HashFunctions.sha256(message)}")
    print(f"SHA-512: {HashFunctions.sha512(message)[:50]}...")
    print(f"SHA-1:   {HashFunctions.sha1(message)}")
    print(f"MD5:     {HashFunctions.md5(message)}")
    
    # Example 2: Demonstrating avalanche effect
    print("\n" + "=" * 50)
    print("AVALANCHE EFFECT (small change = big difference)")
    print("=" * 50)
    
    message1 = "Hello World"
    message2 = "Hello World!"  # Just added an exclamation mark
    
    print(f"\nMessage 1: '{message1}'")
    print(f"SHA-256:   {HashFunctions.sha256(message1)}")
    print(f"\nMessage 2: '{message2}'")
    print(f"SHA-256:   {HashFunctions.sha256(message2)}")
    print("\nNotice how completely different the hashes are!")
    
    # Example 3: HMAC for message authentication
    print("\n" + "=" * 50)
    print("HMAC (MESSAGE AUTHENTICATION)")
    print("=" * 50)
    
    message = "Transfer $1000 to account 12345"
    secret_key = "shared_secret_key"
    
    print(f"\nMessage: {message}")
    print(f"Secret Key: {secret_key}")
    
    mac = HashFunctions.hmac_sha256(message, secret_key)
    print(f"HMAC: {mac}")
    
    # Verify message hasn't been tampered with
    print("\nVerifying message integrity:")
    computed_mac = HashFunctions.hmac_sha256(message, secret_key)
    print(f"Message is authentic: {mac == computed_mac}")
    
    # Try with tampered message
    tampered_message = "Transfer $9000 to account 12345"
    tampered_mac = HashFunctions.hmac_sha256(tampered_message, secret_key)
    print(f"Tampered message is authentic: {mac == tampered_mac}")
    
    # Example 4: Data integrity verification
    print("\n" + "=" * 50)
    print("DATA INTEGRITY VERIFICATION")
    print("=" * 50)
    
    data = "This is important data that must not be modified"
    print(f"\nOriginal data: {data}")
    
    # Compute hash
    data_hash = HashFunctions.sha256(data)
    print(f"Hash: {data_hash}")
    
    # Verify integrity
    is_valid = HashFunctions.verify_integrity(data, data_hash)
    print(f"\nData integrity check: {'PASSED' if is_valid else 'FAILED'}")
    
    # Check with modified data
    modified_data = "This is important data that has been modified"
    is_valid_modified = HashFunctions.verify_integrity(modified_data, data_hash)
    print(f"Modified data integrity check: {'PASSED' if is_valid_modified else 'FAILED'}")


if __name__ == "__main__":
    main()
