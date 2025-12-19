"""Simple Affine cipher helpers over ASCII letters.

Formula:
    E(x) = (a * x + b) mod 26
    D(x) = a_inv * (x - b) mod 26, where gcd(a, 26) = 1

Usage examples:
    encrypted = encrypt("Hello", a=5, b=8)
    decrypted = decrypt(encrypted, a=5, b=8)
"""

from typing import Tuple


def _egcd(a: int, b: int) -> Tuple[int, int, int]:
    """Extended GCD; returns (g, x, y) with g=gcd(a,b) and ax+by=g."""
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = _egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)


def _modinv(a: int, m: int) -> int:
    """Modular inverse of a modulo m; raises if none exists."""
    g, x, _ = _egcd(a, m)
    if g != 1:
        raise ValueError(f"No modular inverse for a={a} mod {m}")
    return x % m


def _encode_char(ch: str, a: int, b: int) -> str:
    """Encode a single ASCII letter; keep case; non-letters untouched."""
    if "A" <= ch <= "Z":
        base = ord("A")
        idx = ord(ch) - base
        return chr(((a * idx + b) % 26) + base)
    if "a" <= ch <= "z":
        base = ord("a")
        idx = ord(ch) - base
        return chr(((a * idx + b) % 26) + base)
    return ch


def _decode_char(ch: str, a_inv: int, b: int) -> str:
    """Decode a single ASCII letter."""
    if "A" <= ch <= "Z":
        base = ord("A")
        idx = ord(ch) - base
        return chr(((a_inv * (idx - b)) % 26) + base)
    if "a" <= ch <= "z":
        base = ord("a")
        idx = ord(ch) - base
        return chr(((a_inv * (idx - b)) % 26) + base)
    return ch


def encrypt(text: str, a: int, b: int) -> str:
    """Affine encryption; requires gcd(a, 26) == 1."""
    _modinv(a, 26)  # Validate invertibility.
    return "".join(_encode_char(ch, a, b) for ch in text)


def decrypt(text: str, a: int, b: int) -> str:
    """Affine decryption using same a, b."""
    a_inv = _modinv(a, 26)
    return "".join(_decode_char(ch, a_inv, b) for ch in text)


if __name__ == "__main__":
    try:
        message = input("Enter text: ")
        a = int(input("Enter multiplier a (coprime with 26): "))
        b = int(input("Enter shift b: "))
    except ValueError:
        raise SystemExit("Parameters a and b must be integers.")

    try:
        encrypted = encrypt(message, a, b)
    except ValueError as exc:
        raise SystemExit(str(exc))

    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypt(encrypted, a, b)}")
