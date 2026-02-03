import hashlib
import hmac


def vulnerable_mac():
    secret = "secret"
    message = input("Enter message: ")

    mac = hashlib.sha256((secret + message).encode("utf-8")).hexdigest()
    print("MAC:", mac)


def secure_hmac():
    secret = b"secret"
    message = input("Enter message: ").encode("utf-8")

    mac = hmac.new(secret, message, hashlib.sha256).hexdigest()
    print("HMAC:", mac)


def main():
    print("Choose option:")
    print("1 - Vulnerable MAC (SHA256(secret || message))")
    print("2 - Secure HMAC (HMAC-SHA256)")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        vulnerable_mac()
    elif choice == "2":
        secure_hmac()
    else:
        print("Invalid option. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
