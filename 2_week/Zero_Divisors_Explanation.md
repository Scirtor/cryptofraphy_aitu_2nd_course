# Zero Divisors: How to Find and Write Them

## Definition of Zero Divisor

A **zero divisor** in a ring is a **nonzero** element **a** such that there exists a **nonzero** element **b** where:
**a · b = 0** (or a · b ≡ 0 mod n)

---

## Finding Zero Divisors in Z_n

### Key Concept:
In **Z_n**, an element **a** is a zero divisor if and only if:
- **gcd(a, n) ≠ 1** (a and n share a common factor)
- **a ≠ 0**

### Why?
If gcd(a, n) = d > 1, then:
- a = d·k for some k
- n = d·m for some m
- Then: a·m = d·k·m = k·(d·m) = k·n ≡ 0 (mod n)
- Since m < n, we have a·m = 0 with m ≠ 0

---

## Example: Z_10

Z_10 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

### Step 1: Exclude 0 (0 is not considered a zero divisor by definition)

### Step 2: Check each element for common factors with 10

**Factors of 10:** 2 and 5

**Elements with gcd ≠ 1:**
- gcd(2, 10) = 2 → **2 is a zero divisor**
- gcd(4, 10) = 2 → **4 is a zero divisor**
- gcd(5, 10) = 5 → **5 is a zero divisor**
- gcd(6, 10) = 2 → **6 is a zero divisor**
- gcd(8, 10) = 2 → **8 is a zero divisor**

**Elements with gcd = 1 (these are NOT zero divisors, they are units):**
- gcd(1, 10) = 1 → unit
- gcd(3, 10) = 1 → unit
- gcd(7, 10) = 1 → unit
- gcd(9, 10) = 1 → unit

### Step 3: Verify by finding the nonzero element that gives 0

Let's verify each zero divisor:

1. **2**: 2 · 5 = 10 ≡ 0 (mod 10) ✓
2. **4**: 4 · 5 = 20 ≡ 0 (mod 10) ✓
3. **5**: 5 · 2 = 10 ≡ 0 (mod 10) or 5 · 4 = 20 ≡ 0 (mod 10) ✓
4. **6**: 6 · 5 = 30 ≡ 0 (mod 10) ✓
5. **8**: 8 · 5 = 40 ≡ 0 (mod 10) ✓

---

## How to Write Zero Divisors

### Option 1: List Notation (Most Common)
```
Zero divisors in Z_10: {2, 4, 5, 6, 8}
```

### Option 2: With Explanation
```
Zero divisors in Z_10: 2, 4, 5, 6, 8
- 2 · 5 = 0
- 4 · 5 = 0
- 5 · 2 = 0
- 6 · 5 = 0
- 8 · 5 = 0
```

### Option 3: Set Notation with Verification
```
Zero divisors in Z_10 = {2, 4, 5, 6, 8}

Verification:
2 · 5 ≡ 0 (mod 10)
4 · 5 ≡ 0 (mod 10)
5 · 2 ≡ 0 (mod 10)
6 · 5 ≡ 0 (mod 10)
8 · 5 ≡ 0 (mod 10)
```

---

## General Method for Any Z_n

For **Z_n** where **n = p₁ᵃ¹ · p₂ᵃ² · ... · pₖᵃᵏ** (prime factorization):

1. **Zero divisors** = all elements **a** where gcd(a, n) > 1
2. **Units** = all elements **a** where gcd(a, n) = 1

---

## Quick Examples

### Z_8:
- Factors of 8: 2
- Zero divisors: {2, 4, 6}
  - 2 · 4 = 8 ≡ 0 (mod 8)
  - 4 · 2 = 8 ≡ 0 (mod 8)
  - 6 · 4 = 24 ≡ 0 (mod 8)

### Z_15 (n = 3 · 5):
- Factors of 15: 3, 5
- Zero divisors: {3, 5, 6, 9, 10, 12}
  - 3 · 5 = 15 ≡ 0 (mod 15)
  - 5 · 3 = 15 ≡ 0 (mod 15)
  - etc.

### Z_7 (prime):
- Since 7 is prime, gcd(a, 7) = 1 for all a ∈ {1, 2, 3, 4, 5, 6}
- **Zero divisors: {}** (empty set - no zero divisors!)
- All nonzero elements are units

---

## Summary for Your Assignment

**For Task 4 (Z_10):**

Zero divisors: **{2, 4, 5, 6, 8}**

You can write it simply as:
```
Zero divisors in Z_10: {2, 4, 5, 6, 8}
```

Or with brief verification:
```
Zero divisors in Z_10: {2, 4, 5, 6, 8}
These are elements that share a common factor with 10 (2 or 5),
making their product with some nonzero element equal to 0 modulo 10.
```


