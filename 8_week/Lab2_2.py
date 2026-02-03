import hashlib

def sha256_binary(input_string):
    h = hashlib.sha256()
    h.update(input_string.encode('utf-8'))
    return bin(int(h.hexdigest(), 16))[2:].zfill(256)

def main():
    message = input("Enter base message: ")
    base_hash = sha256_binary(message)

    print("Character index → Differing hash bits")

    for i in range(len(message)):
        modified = list(message)
        modified[i] = chr(ord(modified[i]) ^ 1)
        modified = "".join(modified)

        new_hash = sha256_binary(modified)

        diff = 0
        for j in range(256):
            if base_hash[j] != new_hash[j]:
                diff += 1

        print(i, "→", diff)

if __name__ == "__main__":
    main()

# Avalanche Experiment