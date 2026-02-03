import hashlib


def compare_sha2_sha3():
    message = input("Enter message: ").encode("utf-8")

    sha256 = hashlib.sha256(message).hexdigest()
    sha3 = hashlib.sha3_256(message).hexdigest()

    print("SHA-256:", sha256)
    print("SHA3-256:", sha3)


def show_analysis():
    print("SHA-256 is faster and widely supported.")
    print("SHA-3 uses a different internal structure and resists length extension attacks.")


def main():
    print("Choose option:")
    print("1 - Compare SHA-256 vs SHA3-256")
    print("2 - Show analysis")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        compare_sha2_sha3()
    elif choice == "2":
        show_analysis()
    else:
        print("Invalid option. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
