import hashlib

def hash_file_sha256(input_string):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()

def main():
    first_input = input("Enter a string to hash: ")
    second_input = input("Enter another string to hash: ")

    first_hash = hash_file_sha256(first_input)
    second_hash = hash_file_sha256(second_input)

    print(f"Hash of first string: {first_hash}")
    print(f"Hash of second string: {second_hash}")

    if first_hash == second_hash:
        print("The hashes are equal.")
    elif first_hash != second_hash:
        print("The hashes are not equal.")
    else:
        print("Unexpected condition.")

if __name__ == "__main__":
    main()