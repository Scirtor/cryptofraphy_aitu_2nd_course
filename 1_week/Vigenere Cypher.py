
from typing import Iterable


def _shift_char_vigenere(char: str, key_char: str) -> str:
    """
    Shift a single ASCII letter by the alphabetical index of key_char, preserving case.
    Non-letters are unchanged.
    """
    if not key_char.isalpha():
        return char

    key_shift = ord(key_char.upper()) - ord("A")
    if "A" <= char <= "Z":
        base = ord("A")
        return chr((ord(char) - base + key_shift) % 26 + base)
    if "a" <= char <= "z":
        base = ord("a")
        return chr((ord(char) - base + key_shift) % 26 + base)
    return char  # Non-letters are unchanged.


def _unshift_char_vigenere(char: str, key_char: str) -> str:
    """
    Unshift a single ASCII letter by the alphabetical index of key_char, preserving case.
    Non-letters are unchanged.
    """
    if not key_char.isalpha():
        return char

    key_shift = ord(key_char.upper()) - ord("A")
    if "A" <= char <= "Z":
        base = ord("A")
        return chr((ord(char) - base - key_shift) % 26 + base)
    if "a" <= char <= "z":
        base = ord("a")
        return chr((ord(char) - base - key_shift) % 26 + base)
    return char  # Non-letters are unchanged.


def _key_stream(text: str, key: str) -> Iterable[str]:
    """
    Generates the key letter for each letter in text, skipping non-letters.
    """
    key = [k for k in key if k.isalpha()]
    key_len = len(key)
    j = 0
    for ch in text:
        if ch.isalpha():
            yield key[j % key_len]
            j += 1
        else:
            yield ch  # For non-letters, yield dummy, will be ignored.


def encrypt(plaintext: str, key: str) -> str:
    """Encrypts plaintext using the Vigenère cipher with the provided key."""
    key_iter = _key_stream(plaintext, key)
    result = []
    for ch in plaintext:
        k = next(key_iter)
        if ch.isalpha():
            result.append(_shift_char_vigenere(ch, k))
        else:
            result.append(ch)
    return "".join(result)


def decrypt(ciphertext: str, key: str) -> str:
    """Decrypts ciphertext using the Vigenère cipher with the provided key."""
    key_iter = _key_stream(ciphertext, key)
    result = []
    for ch in ciphertext:
        k = next(key_iter)
        if ch.isalpha():
            result.append(_unshift_char_vigenere(ch, k))
        else:
            result.append(ch)
    return "".join(result)


if __name__ == "__main__":
    # Minimal CLI interaction for quick testing.
    try:
        message = input("Enter text: ")
        key = input("Enter Vigenere key: ")
        if not key or not key.isalpha():
            raise ValueError
    except ValueError:
        raise SystemExit("Key must be a non-empty string of alphabetic characters.")

    encrypted = encrypt(message, key)
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypt(encrypted, key)}")

