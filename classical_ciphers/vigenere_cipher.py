"""
Vigenère Cipher Implementation

The Vigenère cipher is a method of encrypting alphabetic text by using a series of 
interwoven Caesar ciphers based on the letters of a keyword. It is a form of 
polyalphabetic substitution.

The encryption of the original text is done using the Vigenère square or Vigenère table.

Author: AITU Cryptography Course
"""


class VigenereCipher:
    """
    Vigenère cipher implementation for encryption and decryption.
    
    Attributes:
        key (str): The keyword used for encryption/decryption
    """
    
    def __init__(self, key):
        """
        Initialize the Vigenère cipher with a keyword.
        
        Args:
            key (str): The keyword to use for encryption (must contain only letters)
            
        Raises:
            ValueError: If key is empty or contains non-alphabetic characters
        """
        if not key or not key.isalpha():
            raise ValueError("Key must be a non-empty string containing only letters")
        self.key = key.upper()
    
    def _extend_key(self, text_length):
        """
        Extend the key to match the length of the text.
        
        Args:
            text_length (int): Length of text to match
            
        Returns:
            str: Extended key
        """
        extended_key = ""
        key_index = 0
        
        for _ in range(text_length):
            extended_key += self.key[key_index % len(self.key)]
            key_index += 1
        
        return extended_key
    
    def encrypt(self, plaintext):
        """
        Encrypt plaintext using Vigenère cipher.
        
        Args:
            plaintext (str): The text to encrypt
            
        Returns:
            str: The encrypted text (ciphertext)
            
        Example:
            >>> cipher = VigenereCipher("KEY")
            >>> cipher.encrypt("HELLO")
            'RIJVS'
        """
        ciphertext = []
        key_index = 0
        
        for char in plaintext:
            if char.isalpha():
                # Determine if uppercase or lowercase
                is_upper = char.isupper()
                char = char.upper()
                
                # Get the shift from the key
                shift = ord(self.key[key_index % len(self.key)]) - ord('A')
                
                # Encrypt the character
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                
                # Preserve original case
                if not is_upper:
                    encrypted_char = encrypted_char.lower()
                
                ciphertext.append(encrypted_char)
                key_index += 1
            else:
                # Keep non-alphabetic characters as is
                ciphertext.append(char)
        
        return ''.join(ciphertext)
    
    def decrypt(self, ciphertext):
        """
        Decrypt ciphertext using Vigenère cipher.
        
        Args:
            ciphertext (str): The text to decrypt
            
        Returns:
            str: The decrypted text (plaintext)
            
        Example:
            >>> cipher = VigenereCipher("KEY")
            >>> cipher.decrypt("RIJVS")
            'HELLO'
        """
        plaintext = []
        key_index = 0
        
        for char in ciphertext:
            if char.isalpha():
                # Determine if uppercase or lowercase
                is_upper = char.isupper()
                char = char.upper()
                
                # Get the shift from the key
                shift = ord(self.key[key_index % len(self.key)]) - ord('A')
                
                # Decrypt the character
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                
                # Preserve original case
                if not is_upper:
                    decrypted_char = decrypted_char.lower()
                
                plaintext.append(decrypted_char)
                key_index += 1
            else:
                # Keep non-alphabetic characters as is
                plaintext.append(char)
        
        return ''.join(plaintext)


def main():
    """
    Demonstration of Vigenère cipher usage.
    """
    print("=" * 50)
    print("VIGENÈRE CIPHER DEMONSTRATION")
    print("=" * 50)
    
    # Example 1: Basic encryption and decryption
    key = "CRYPTO"
    cipher = VigenereCipher(key)
    plaintext = "HELLO WORLD"
    
    print(f"\nKey: {key}")
    print(f"Original text: {plaintext}")
    encrypted = cipher.encrypt(plaintext)
    print(f"Encrypted text: {encrypted}")
    decrypted = cipher.decrypt(encrypted)
    print(f"Decrypted text: {decrypted}")
    
    # Example 2: Longer text with mixed case
    key2 = "SECRETKEY"
    cipher2 = VigenereCipher(key2)
    plaintext2 = "The Quick Brown Fox Jumps Over The Lazy Dog"
    
    print(f"\n\nKey: {key2}")
    print(f"Original text: {plaintext2}")
    encrypted2 = cipher2.encrypt(plaintext2)
    print(f"Encrypted text: {encrypted2}")
    decrypted2 = cipher2.decrypt(encrypted2)
    print(f"Decrypted text: {decrypted2}")
    
    # Example 3: Famous historical example
    key3 = "LEMON"
    cipher3 = VigenereCipher(key3)
    plaintext3 = "ATTACK AT DAWN"
    
    print(f"\n\nKey: {key3}")
    print(f"Original text: {plaintext3}")
    encrypted3 = cipher3.encrypt(plaintext3)
    print(f"Encrypted text: {encrypted3}")
    decrypted3 = cipher3.decrypt(encrypted3)
    print(f"Decrypted text: {decrypted3}")


if __name__ == "__main__":
    main()
