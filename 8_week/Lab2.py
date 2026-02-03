import hashlib

def sha256_to_binary(input_string):
    sha = hashlib.sha256()
    sha.update(input_string.encode('utf-8'))
    hex_hash = sha.hexdigest()
    return bin(int(hex_hash, 16))[2:].zfill(256)

def count_different_bits(bin1, bin2):
    diff = 0
    for i in range(256):
        if bin1[i] != bin2[i]:
            diff += 1
    return diff

def main():
    msg1 = input("Enter first message: ")
    msg2 = input("Enter second message: ")

    hash1 = sha256_to_binary(msg1)
    hash2 = sha256_to_binary(msg2)

    diff_bits = count_different_bits(hash1, hash2)

    print("Number of differing bits:", diff_bits)

if __name__ == "__main__":
    main()
