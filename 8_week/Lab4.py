import hashlib
import os


def hash_plain():
    password = input("Enter password: ")
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password.encode("utf-8"))
    print("Stored hash:", sha256_hash.hexdigest())


def hash_with_salt():
    password = input("Enter password: ")
    salt = os.urandom(8)

    sha256_hash = hashlib.sha256()
    sha256_hash.update(salt + password.encode("utf-8"))

    print("Salt:", salt.hex())
    print("Hash:", sha256_hash.hexdigest())


def main():
    print("Choose option:")
    print("1 - Hash password (no salt)")
    print("2 - Hash password with salt")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        hash_plain()
    elif choice == "2":
        hash_with_salt()
    else:
        print("Invalid option. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
