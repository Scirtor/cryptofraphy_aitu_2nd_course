import hashlib

def hash_file_sha256(filename):
    sha256_hash = hashlib.sha256()
    file = open(filename, "rb")

    while True:
        block = file.read(4096)
        if not block:
            break
        sha256_hash.update(block)

    file.close()
    return sha256_hash.hexdigest()

def main():
    filename = input("Enter filename: ")
    print("File SHA-256:", hash_file_sha256(filename))

if __name__ == "__main__":
    main()
