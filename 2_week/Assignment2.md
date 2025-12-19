# Assignment 2

# Bekmurat Nurzhan

# CS-2406

## Task 1 Basic

### 1)

    37 mod 8
    a = q * m + r;   0 <= r < m
    m = 8
    a = 37
    r - ?
    r = 37 - q * 8;  0 <= r < 8
    r = 37 - 32 = 5; 0 <= 5 < 8

### 2)

    -15 mod 7
    a = q * m + r
    m = 7
    a = -15
    r - ?
    r = -15 - q * 7; 0 <=              r < m
    r != -15 - 2 * 7 = -29;            r !< 0
    r != -15 - (-2) * 7 = -1;          r !< 0
    r = -15 - (-3) * 7 = -15 + 21 = 6; 0 <= 6 < 7
    q = -3
    r = 6

### 3)

    1234 mod 9
    a = q * m + r;    0 <= r < m
    a = 1234
    m = 9
    r - ?
    manual calculation takes to long
    I use calculator here
    1234 = q * 9 + r; 0 <= r < 9
    r = 1234 - q * 9; 0 <= r < 9
    r = 1234 - 1233;  9 * 137 = 1233
    r = 1
    q = 137

## Task 2 Congruence

### 1)

    91 ≡ 13(mod 13)
    Checking 91 / 13 = 7(0)
    Answer: expression 91 ≡ 13(mod 13) is False

### 2)

    5^4≡1(mod4)
    Checking 5^4 = 5 * 5 * 5 * 5 = 125 * 5 = 525; 525 / 4 = 131(1)
    Answer: expression 5^4≡1(mod4) is True

### 3)

    If a≡b(modn), then a^2≡b^2 (modn)
    
    If a ≡ b (mod n), then a - b = kn for some integer k.
    a² - b² = (a - b)(a + b) = kn(a + b) = n[k(a + b)]
    So n divides (a² - b²), which means a² ≡ b² (mod n).
    
    Answer: True

## Task 3 Structure

    Describe the set of residues modulo 6 and construct the addition table for Z_6.

  | Table | 0 | 1 | 2 | 3 | 4 | 5 |
  | - | - | - | - | - | - | - |
  | 0 | 0 | 1 | 2 | 3 | 4 | 5 |
  | 1 | 1 | 2 | 3 | 4 | 5 | 0 |
  | 2 | 2 | 3 | 4 | 5 | 0 | 1 |
  | 3 | 3 | 4 | 5 | 0 | 1 | 2 |
  | 4 | 4 | 5 | 0 | 1 | 2 | 3 |
  | 5 | 5 | 0 | 1 | 2 | 3 | 4 |

## Task 4 For thering Z_10:

### 1) Find all zero divisors
    Greatest common divisors between members and limit 10.
    1 * 10 = 10 * 1 --> 10 is not in array Z_10 = [0, 1, 2, 3, 4 ,5, 6, 7, 8, 9]
    2 * 5  = 10 * 1 --> 5 is in Z_10 = [0, 1, 2, 3, 4 ,5, 6, 7, 8, 9]
    3 * 10 = 10 * 3 --> 10 not in 10 arr Z_10 =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    4 * 5 = 20 = 10 * 2 --> 5 is in array Z_10 =[0, 1, 2, 3, 4 ,5, 6, 7, 8, 9]
    5 * 2 = 10 * 1--> 2 is in array Z_10 = [0, 1, 2, 3, 4 ,5, 6, 7, 8, 9]
    6 * 5 = 10 = 10 * 3 --> 5 is in array Z_10 = [0, 1, 2, 3, 4 ,5, 6, 7, 8, 9]
    7 * 10 = 70 = 10 * 7 --> 10 is not in array Z_10 = [0, 1, 2, 3, 4 ,5, 6, 7, 8, 9]
    8 * 5 = 40 = 10 * 4 --> 5 is in array Z_10 = [0, 1, 2, 3, 4 ,5, 6, 7, 8, 9]
    9 * 10 = 90 = 10 * 9 --> 10 is not in array Z_10 = [0, 1, 2, 3, 4 ,5, 6, 7, 8, 9]

    According to my calculations all Zero Divisor elements in Z_10 are [2, 4, 5, 6, 8]

    2 · 5 = 10 ≡ 0 (mod 10)
    4 · 5 = 20 ≡ 0 (mod 10)
    5 · 2 = 10 ≡ 0 (mod 10)
    6 · 5 = 30 ≡ 0 (mod 10)
    8 · 5 = 40 ≡ 0 (mod 10)


### 2) Find all units
    Units in Z_10: {1, 3, 7, 9}
    
    Units are elements with gcd(a, 10) = 1.
    - gcd(1, 10) = 1 → unit
    - gcd(3, 10) = 1 → unit
    - gcd(7, 10) = 1 → unit
    - gcd(9, 10) = 1 → unit

### 3) Identify elements that do not have multiplicative inverses
    Elements without multiplicative inverses in Z_10: {0, 2, 4, 5, 6, 8}
    
    These are the zero divisors and 0.

## Task 5 (Theory)

Prove that Z_n is a field if and only if n is a prime number.

    If n is prime:
    - For any nonzero a in Z_n, gcd(a, n) = 1
    - So a has a multiplicative inverse
    - Therefore Z_n is a field
    
    If Z_n is a field:
    - Every nonzero element has an inverse
    - If n is composite, say n = ab with 1 < a, b < n
    - Then a · b = n ≡ 0 (mod n)
    - So a and b are zero divisors and cannot have inverses
    - Contradiction! So n must be prime.
    
    Therefore, Z_n is a field if and only if n is prime.

## Task 6

Determine whether the ring Z_8 is an integral domain.

    Z_8 = {0, 1, 2, 3, 4, 5, 6, 7}
    
    Check for zero divisors:
    2 · 4 = 8 ≡ 0 (mod 8)
    
    Since 2 and 4 are nonzero but their product is 0, Z_8 has zero divisors.
    Therefore Z_8 is NOT an integral domain.

## Task 7

Compute:  
7^123 mod 11

By Fermat’s little theorem:  
7^10 ≡ 1 (mod 11)

Reduce the exponent:  
123 ≡ 3 (mod 10)

So:  
7^123 ≡ 7^3 = 343 ≡ 2 (mod 11)

**Answer:** 2

---

## Task 8

Compare the number of operations when computing:  
a^1024 mod n

### Naive exponentiation

a^1024 = a · a · ... · a (1024 times)

- Multiplications: 1023  
- Time complexity: O(k)

### Binary (fast) exponentiation

1024 = 2^10

- Squarings: 10  
- Extra multiplications: 0  
- Total operations: ≈ 10  
- Time complexity: O(log k)

## Task 9 (Algorithmic)

Describe an algorithm that computes

a^k  mod  n

in O(log k) time.

    Algorithm:
    ```
    result = 1
    base = a mod n
    
    while k > 0:
        if k is odd:
            result = (result * base) mod n
        base = (base * base) mod n
        k = k / 2
    
    return result
    ```
    
    This works by using binary representation of k. Each iteration processes one bit.
    Time complexity: O(log k) because we process log₂(k) bits.

## Task 10

    Determine whether the following rings are fields:

### 1) Z_9

    Z_9 is NOT a field because 9 is not prime (9 = 3²).
    Example: 3 · 3 = 9 ≡ 0 (mod 9), so 3 is a zero divisor.

### 2) Z_11

    Z_11 IS a field because 11 is prime.

### 3) Z_15

    Z_15 is NOT a field because 15 is not prime (15 = 3 · 5).
    Example: 3 · 5 = 15 ≡ 0 (mod 15), so 3 and 5 are zero divisors.

## Task 11

    Let F_7

### 1) Find the multiplicative inverse of each nonzero element

    1⁻¹ = 1 (since 1 · 1 = 1)
    2⁻¹ = 4 (since 2 · 4 = 8 ≡ 1 mod 7)
    3⁻¹ = 5 (since 3 · 5 = 15 ≡ 1 mod 7)
    4⁻¹ = 2 (since 4 · 2 = 8 ≡ 1 mod 7)
    5⁻¹ = 3 (since 5 · 3 = 15 ≡ 1 mod 7)
    6⁻¹ = 6 (since 6 · 6 = 36 ≡ 1 mod 7)

### 2) Verify that every nonzero element has an inverse

    Since 7 is prime, gcd(a, 7) = 1 for all a in {1, 2, 3, 4, 5, 6}.
    So every nonzero element has an inverse. F_7 is a field.

## Task 12 (Core)

    Find all primitive elements of the field F_7
    
    Test each element to find order 6:
    
    1: order = 1
    2: 2³ = 8 ≡ 1 mod 7, order = 3
    3: 3⁶ = 15 ≡ 1 mod 7, order = 6 ✓
    4: 4³ = 8 ≡ 1 mod 7, order = 3
    5: 5⁶ = 15 ≡ 1 mod 7, order = 6 ✓
    6: 6² = 36 ≡ 1 mod 7, order = 2
    
    Primitive elements: {3, 5}

## Task 13

Prove that the multiplicative group has order q-1

    F_q has q elements: {0, 1, 2, ..., q-1}
    F_q* = F_q \ {0} (all nonzero elements)
    
    Since F_q has q elements and 0 is not in F_q*, we have:
    |F_q*| = q - 1

## Task 14 (Advanced)

    Let F_11

### 1) Find an element of order 10

    Test 2:
    2¹ = 2
    2² = 4
    2⁵ = 32 ≡ 10 mod 11
    2¹⁰ = 100 ≡ 1 mod 11
    
    Check divisors: 2¹ ≠ 1, 2² ≠ 1, 2⁵ ≠ 1, 2¹⁰ = 1
    So order of 2 is 10.

### 2) Verify that it generates the multiplicative group

    Powers of 2: {2⁰, 2¹, ..., 2⁹} = {1, 2, 4, 8, 5, 10, 9, 7, 3, 6} = F_11*
    So 2 generates F_11*.

## Task 15 (Theoretical)

Prove that the multiplicative group of any finite field is cyclic

    Let |F_q*| = n = q - 1.
    
    For each divisor d of n, let ψ(d) be the number of elements of order d.
    By Lagrange's theorem, every element has order dividing n.
    
    If an element has order d, it's a root of xᵈ - 1. Over a field, this polynomial has at most d roots.
    So ψ(d) ≤ φ(d) for all d.
    
    We have Σ(d|n) ψ(d) = n and Σ(d|n) φ(d) = n.
    Since ψ(d) ≤ φ(d) and the sums are equal, we must have ψ(d) = φ(d) for all d.
    
    In particular, ψ(n) = φ(n) > 0, so there exists an element of order n.
    This element generates F_q*, so F_q* is cyclic.

## Task 16

    Let n = pq, where p and q are distinct primes.

### 1) Is Z_n a field?

    No, Z_n is NOT a field because n = pq is composite.
    Since p · q = n ≡ 0 (mod n), p and q are zero divisors and cannot have inverses.

### 2) Find zero divisors in Z_n

    Zero divisors are elements with gcd(a, n) > 1.
    Since n = pq, the zero divisors are:
    - Multiples of p: {p, 2p, 3p, ..., (q-1)p}
    - Multiples of q: {q, 2q, 3q, ..., (p-1)q}
    
    Example: n = 15 = 3 · 5
    Zero divisors: {3, 5, 6, 9, 10, 12}

## Task 17 (Cryptography-Inspired)

    Let p = 23, g = 5

### 1) Verify whether g is a generator of Z_23*

    |Z_23*| = 22
    Check if order of 5 is 22:
    
    Proper divisors of 22: 1, 2, 11
    5¹ = 5 ≠ 1
    5² = 25 ≡ 2 ≠ 1
    5¹¹ = 22 ≠ 1 (from part 2)
    5²² = (5¹¹)² = 22² = 484 ≡ 1 mod 23
    
    Since 5²² = 1 and no smaller power equals 1, order of 5 is 22.
    So 5 IS a generator of Z_23*.

### 2) Compute 5^11 mod 23

    11 = 1011₂ = 8 + 2 + 1
    
    5¹ mod 23 = 5
    5² mod 23 = 2
    5⁴ mod 23 = 4
    5⁸ mod 23 = 16
    
    5¹¹ mod 23 = 5⁸ · 5² · 5¹ = 16 · 2 · 5 = 160 ≡ 22 mod 23
    
    Answer: 5¹¹ mod 23 = 22
