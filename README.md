# Cryptography AITU 2nd Course

A comprehensive repository for cryptography implementations and educational materials, including various cipher implementations, encryption algorithms, and cryptographic primitives.

## 📚 Repository Structure

```
cryptofraphy_aitu_2nd_course/
├── classical_ciphers/     # Classical encryption algorithms
│   ├── caesar_cipher.py   # Caesar cipher implementation
│   ├── vigenere_cipher.py # Vigenère cipher implementation
│   └── substitution_cipher.py
├── symmetric_ciphers/     # Symmetric key cryptography
│   ├── aes_example.py     # AES implementation examples
│   └── des_example.py     # DES implementation examples
├── asymmetric_ciphers/    # Asymmetric key cryptography
│   ├── rsa_cipher.py      # RSA implementation
│   └── ecc_example.py     # Elliptic curve cryptography
├── hash_functions/        # Cryptographic hash functions
│   ├── sha_example.py     # SHA implementations
│   └── md5_example.py     # MD5 examples
├── examples/              # Usage examples and demonstrations
├── tests/                 # Unit tests for implementations
└── README.md             # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Scirtor/cryptofraphy_aitu_2nd_course.git
cd cryptofraphy_aitu_2nd_course
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies (if any):
```bash
pip install -r requirements.txt
```

## 📖 Usage Examples

### Classical Ciphers

#### Caesar Cipher
```python
from classical_ciphers.caesar_cipher import CaesarCipher

cipher = CaesarCipher(shift=3)
encrypted = cipher.encrypt("HELLO WORLD")
decrypted = cipher.decrypt(encrypted)
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
```

## 🔐 Cipher Categories

### Classical Ciphers
- **Caesar Cipher**: Simple substitution cipher with fixed shift
- **Vigenère Cipher**: Polyalphabetic substitution using keyword
- **Substitution Cipher**: Letter-to-letter mapping

### Symmetric Ciphers
- **AES**: Advanced Encryption Standard
- **DES**: Data Encryption Standard

### Asymmetric Ciphers
- **RSA**: Rivest-Shamir-Adleman algorithm
- **ECC**: Elliptic Curve Cryptography

### Hash Functions
- **SHA-256**: Secure Hash Algorithm
- **MD5**: Message Digest Algorithm

## 🧪 Running Tests

```bash
python -m pytest tests/
```

## 📝 Contributing

Feel free to add more cipher implementations, improve existing code, or add documentation. When contributing:

1. Follow Python PEP 8 style guidelines
2. Add docstrings to all functions and classes
3. Include unit tests for new implementations
4. Update this README if adding new categories or ciphers

## 📚 Educational Resources

This repository is designed for educational purposes. Each implementation includes:
- Detailed comments explaining the algorithm
- Example usage
- References to cryptographic principles

## ⚠️ Security Notice

**WARNING**: These implementations are for educational purposes only. Do not use them in production systems or for securing sensitive data. Always use well-tested, industry-standard cryptographic libraries for real-world applications.

## 📄 License

This project is for educational use at AITU (Astana IT University).

## 👥 Authors

- AITU 2nd Course Students

## 🔗 References

- [Cryptography and Network Security by William Stallings](https://www.pearson.com/store/p/cryptography-and-network-security-principles-and-practice/P100000583355)
- [Applied Cryptography by Bruce Schneier](https://www.schneier.com/books/applied_cryptography/)
- [Introduction to Modern Cryptography by Katz and Lindell](https://www.cs.umd.edu/~jkatz/imc.html)