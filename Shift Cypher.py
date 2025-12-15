"""Simple shift (Caesar) cipher helpers.

Usage examples:
    encrypted = encrypt("Hello, World!", 3)
    decrypted = decrypt(encrypted, 3)
"""

from typing import Iterable


def _shift_char(char: str, shift: int) -> str:
    """Shift a single ASCII letter by `shift`, preserving case."""
    if "A" <= char <= "Z":
        base = ord("A")
        return chr((ord(char) - base + shift) % 26 + base)
    if "a" <= char <= "z":
        base = ord("a")
        return chr((ord(char) - base + shift) % 26 + base)
    return char  # Non-letters are unchanged.


def encrypt(text: str, shift: int) -> str:
    """Encrypt text with a shift (Caesar) cipher."""
    return "".join(_shift_char(c, shift) for c in text)


def decrypt(text: str, shift: int) -> str:
    """Decrypt text that was encrypted with the same shift value."""
    return encrypt(text, -shift)


if __name__ == "__main__":
    # Minimal CLI interaction for quick testing.
    try:
        message = input("Enter text: ")
        amount = int(input("Enter shift (e.g., 3): "))
    except ValueError:
        raise SystemExit("Shift must be an integer.")

    encrypted = encrypt(message, amount)
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypt(encrypted, amount)}")
