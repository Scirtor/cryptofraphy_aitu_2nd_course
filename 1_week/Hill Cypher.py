def hill_cypher():
    M = [[2, 3], [5, 7]]
    Minv = [[19, 3], [5, 24]]  # precomputed inverse of M mod 26

    def sanitize(s):
        return [ord(c) - 97 for c in s.lower() if c.isalpha()]

    def to_text(nums):
        return ''.join(chr(n % 26 + 97) for n in nums)

    mode = input("Encrypt (e) or Decrypt (d)? ").strip().lower()
    text = input("Input text: ")
    nums = sanitize(text)
    if len(nums) % 2 == 1:
        nums.append(ord('x') - 97)

    out = []
    for i in range(0, len(nums), 2):
        a, b = nums[i], nums[i + 1]
        if mode.startswith('d'):
            r0 = (Minv[0][0] * a + Minv[0][1] * b) % 26
            r1 = (Minv[1][0] * a + Minv[1][1] * b) % 26
        else:
            r0 = (M[0][0] * a + M[0][1] * b) % 26
            r1 = (M[1][0] * a + M[1][1] * b) % 26
        out.extend([r0, r1])

    result = to_text(out)
    print(result)
    return result

def main():
    hill_cypher()

if __name__ == "__main__":
    main()