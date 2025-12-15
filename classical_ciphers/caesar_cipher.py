"""
Caesar Cipher Implementation

The Caesar cipher is one of the simplest and most widely known encryption techniques.
It is a type of substitution cipher in which each letter in the plaintext is replaced
by a letter some fixed number of positions down the alphabet.

For example, with a shift of 3:
- A would be replaced by D
- B would be replaced by E
- and so on...

Author: AITU Cryptography Course
"""


class CaesarCipher:
    """
    Caesar cipher implementation for encryption and decryption.
    
    Attributes:
        shift (int): The number of positions to shift each letter
    """
    
    def __init__(self, shift=3):
        """
        Initialize the Caesar cipher with a specific shift value.
        
        Args:
            shift (int): Number of positions to shift (default is 3)
        """
        self.shift = shift % 26  # Ensure shift is within 0-25
    
    def encrypt(self, plaintext):
        """
        Encrypt plaintext using Caesar cipher.
        
        Args:
            plaintext (str): The text to encrypt
            
        Returns:
            str: The encrypted text (ciphertext)
            
        Example:
            >>> cipher = CaesarCipher(shift=3)
            >>> cipher.encrypt("HELLO")
            'KHOOR'
        """
        ciphertext = []
        
        for char in plaintext:
            if char.isalpha():
                # Determine if uppercase or lowercase
                ascii_offset = ord('A') if char.isupper() else ord('a')
                
                # Shift the character
                shifted = (ord(char) - ascii_offset + self.shift) % 26
                encrypted_char = chr(shifted + ascii_offset)
                ciphertext.append(encrypted_char)
            else:
                # Keep non-alphabetic characters as is
                ciphertext.append(char)
        
        return ''.join(ciphertext)
    
    def decrypt(self, ciphertext):
        """
        Decrypt ciphertext using Caesar cipher.
        
        Args:
            ciphertext (str): The text to decrypt
            
        Returns:
            str: The decrypted text (plaintext)
            
        Example:
            >>> cipher = CaesarCipher(shift=3)
            >>> cipher.decrypt("KHOOR")
            'HELLO'
        """
        # Decryption is encryption with negative shift
        original_shift = self.shift
        self.shift = (26 - self.shift) % 26
        plaintext = self.encrypt(ciphertext)
        self.shift = original_shift
        return plaintext
    
    def brute_force(self, ciphertext):
        """
        Attempt to decrypt using all possible shifts (brute force attack).
        
        Args:
            ciphertext (str): The text to decrypt
            
        Returns:
            list: List of tuples containing (shift, decrypted_text)
            
        Example:
            >>> cipher = CaesarCipher()
            >>> results = cipher.brute_force("KHOOR")
            >>> for shift, text in results:
            ...     print(f"Shift {shift}: {text}")
        """
        results = []
        for shift in range(26):
            temp_cipher = CaesarCipher(shift)
            decrypted = temp_cipher.decrypt(ciphertext)
            results.append((shift, decrypted))
        return results


def main():
    """
    Demonstration of Caesar cipher usage.
    """
    print("=" * 50)
    print("CAESAR CIPHER DEMONSTRATION")
    print("=" * 50)
    
    # Example 1: Basic encryption and decryption
    cipher = CaesarCipher(shift=3)
    plaintext = "HELLO WORLD"
    
    print(f"\nOriginal text: {plaintext}")
    encrypted = cipher.encrypt(plaintext)
    print(f"Encrypted text (shift=3): {encrypted}")
    decrypted = cipher.decrypt(encrypted)
    print(f"Decrypted text: {decrypted}")
    
    # Example 2: Different shift value
    cipher2 = CaesarCipher(shift=13)  # ROT13
    plaintext2 = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    print(f"\n\nOriginal text: {plaintext2}")
    encrypted2 = cipher2.encrypt(plaintext2)
    print(f"Encrypted text (shift=13/ROT13): {encrypted2}")
    decrypted2 = cipher2.decrypt(encrypted2)
    print(f"Decrypted text: {decrypted2}")
    
    # Example 3: Brute force attack
    print(f"\n\nBrute Force Attack on: {encrypted}")
    print("-" * 50)
    results = cipher.brute_force(encrypted)
    for shift, text in results[:5]:  # Show first 5 results
        print(f"Shift {shift:2d}: {text}")
    print("...")


if __name__ == "__main__":
    main()
