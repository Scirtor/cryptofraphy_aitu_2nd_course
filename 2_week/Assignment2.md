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
    Don't know how to solve this now

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
    
    Definition: A unit is an element that has a multiplicative inverse.
    An element a in Z_n is a unit if and only if gcd(a, n) = 1.
    
    Check gcd with 10:
    - gcd(1, 10) = 1 → unit (1⁻¹ = 1)
    - gcd(2, 10) = 2 → not a unit
    - gcd(3, 10) = 1 → unit (3⁻¹ = 7, since 3 · 7 = 21 ≡ 1 mod 10)
    - gcd(4, 10) = 2 → not a unit
    - gcd(5, 10) = 5 → not a unit
    - gcd(6, 10) = 2 → not a unit
    - gcd(7, 10) = 1 → unit (7⁻¹ = 3, since 7 · 3 = 21 ≡ 1 mod 10)
    - gcd(8, 10) = 2 → not a unit
    - gcd(9, 10) = 1 → unit (9⁻¹ = 9, since 9 · 9 = 81 ≡ 1 mod 10)
    
    Multiplicative inverses:
    - 1⁻¹ = 1
    - 3⁻¹ = 7
    - 7⁻¹ = 3
    - 9⁻¹ = 9

### 3) Identify elements that do not have multiplicative inverses
    Elements without multiplicative inverses in Z_10: {0, 2, 4, 5, 6, 8}
    
    - 0: Never has an inverse (0 · anything = 0, never 1)
    - 2, 4, 5, 6, 8: These are zero divisors (gcd(a, 10) > 1), 
      and zero divisors cannot have inverses because if a·b = 0 
      and a had an inverse, we'd get b = 0, a contradiction.

## Task 5 (Theory)

Prove that Z_n is a field if and only if n is a prime number.

    Proof:
    
    A field is a commutative ring where every nonzero element has a multiplicative inverse.
    
    Part 1: If n is prime, then Z_n is a field (⇒)
    
    Assume n is prime.
    - Z_n = {0, 1, 2, ..., n-1}
    - For any nonzero element a ∈ Z_n (where 1 ≤ a ≤ n-1):
      * Since n is prime and 1 ≤ a < n, we have gcd(a, n) = 1
      * By Bézout's identity, there exist integers x, y such that ax + ny = 1
      * Taking this equation mod n: ax ≡ 1 (mod n)
      * Therefore, x mod n is the multiplicative inverse of a
    - Every nonzero element has an inverse, so Z_n is a field.
    
    Part 2: If Z_n is a field, then n is prime (⇐)
    
    Assume Z_n is a field. We prove n must be prime by contradiction.
    
    Suppose n is composite (not prime). Then n = ab where 1 < a < n and 1 < b < n.
    - Both a and b are nonzero elements in Z_n
    - But a · b = n ≡ 0 (mod n)
    - This means a · b = 0, so a and b are zero divisors
    - If a has a multiplicative inverse a⁻¹, then:
      * a · b = 0
      * a⁻¹ · (a · b) = a⁻¹ · 0
      * (a⁻¹ · a) · b = 0
      * 1 · b = 0
      * b = 0
    - But b ≠ 0 (since 1 < b < n), which is a contradiction!
    - Therefore, a cannot have a multiplicative inverse.
    - This contradicts our assumption that Z_n is a field.
    
    Conclusion: Z_n is a field if and only if n is prime. ∎
    
    Key insight: In Z_n, an element a has a multiplicative inverse if and only if 
    gcd(a, n) = 1. When n is prime, gcd(a, n) = 1 for all nonzero a, so every 
    nonzero element has an inverse.

## Task 6

Determine whether the ring Z_8 is an integral domain.

    Definition: An integral domain is a commutative ring with unity (1) 
    that has NO zero divisors.
    
    A zero divisor is a nonzero element a such that a·b = 0 for some nonzero b.
    
    Z_8 = {0, 1, 2, 3, 4, 5, 6, 7}
    
    Check for zero divisors:
    2 · 4 = 8 ≡ 0 (mod 8)  → 2 and 4 are both nonzero, but their product is 0
    
    Since we found zero divisors (2 and 4), Z_8 is NOT an integral domain.
    
    Additional zero divisor pairs in Z_8:
    - 2 · 4 = 8 ≡ 0 (mod 8)
    - 4 · 2 = 8 ≡ 0 (mod 8)
    - 4 · 6 = 24 ≡ 0 (mod 8)
    - 6 · 4 = 24 ≡ 0 (mod 8)
    
    Answer: Z_8 is NOT an integral domain because it contains zero divisors.
    
    Note: Z_n is an integral domain if and only if n is prime.

## Task 7

Compute using fast modular exponentiation:

7^123  mod 11

## Task 8

Compare the number of operations required for:

naiveexponentiation

binary (fast) exponentiation

when computing a^1024 mod n.

## Task 9 (Algorithmic)

Describe an algorithm that computes

a^k  mod  n

in O(log⁡ k)time.

## Task 10

    Determine whether the following rings are fields:

### 1) Z_9

### 2) Z_11

### 3) Z_15

## Task 11

    Let F_7

### 1) Find the multiplicative inverse of each nonzero element

### 2) Verify that every nonzero element has an inverse

## Task 12 (Core)

    Find all primitive elements of the field F_7

## Task 13

Prove that the multiplicative group has order q-1

## Task 14 (Advanced)

    Let F_11

### 1) Find an element of order 10

### 2) Verify that it generates the multiplicative group

## Task 15 (Theoretical)

Prove that the multiplicative group of any finite field is cyclic

## Task 16

    Let n = pq, where p and q are distinct primes.

### 1) Is Z_n a field?

### 2) Find zero divizors in Z_n

## Task 17 (Cryptography-Inspired)

    Let p = 23, g =5

### 1) Verify whether g is a generator of

### 2) Compute 5^11 mod 23
