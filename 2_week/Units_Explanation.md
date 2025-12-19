# Units: How to Find and Write Them

## Definition of Unit

A **unit** in a ring is an element **a** that has a **multiplicative inverse**.
That is, there exists an element **b** such that:
**a · b = 1** (or a · b ≡ 1 mod n)

We call **b** the **multiplicative inverse** of **a**, denoted as **a⁻¹** or **1/a**.

---

## Finding Units in Z_n

### Key Theorem:
In **Z_n**, an element **a** is a unit if and only if:
**gcd(a, n) = 1**

This means **a** and **n** are **coprime** (relatively prime).

### Why?
By **Bézout's Identity** (Extended Euclidean Algorithm):
- If gcd(a, n) = 1, then there exist integers x, y such that: **a·x + n·y = 1**
- Taking modulo n: **a·x ≡ 1 (mod n)**
- Therefore, x is the multiplicative inverse of a

---

## Example: Z_10

Z_10 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

### Step 1: Exclude 0 (0 never has an inverse)

### Step 2: Check gcd with 10 for each element

**Check each element:**

| Element | gcd(a, 10) | Is Unit? | Why? |
|---------|------------|----------|------|
| 0 | - | No | 0 never has an inverse |
| 1 | gcd(1, 10) = 1 | **YES** | 1 · 1 = 1 |
| 2 | gcd(2, 10) = 2 | No | Zero divisor |
| 3 | gcd(3, 10) = 1 | **YES** | 3 · 7 = 21 ≡ 1 (mod 10) |
| 4 | gcd(4, 10) = 2 | No | Zero divisor |
| 5 | gcd(5, 10) = 5 | No | Zero divisor |
| 6 | gcd(6, 10) = 2 | No | Zero divisor |
| 7 | gcd(7, 10) = 1 | **YES** | 7 · 3 = 21 ≡ 1 (mod 10) |
| 8 | gcd(8, 10) = 2 | No | Zero divisor |
| 9 | gcd(9, 10) = 1 | **YES** | 9 · 9 = 81 ≡ 1 (mod 10) |

### Step 3: Find the inverses

Let's find the multiplicative inverse for each unit:

1. **1**: 1 · 1 = 1, so **1⁻¹ = 1**

2. **3**: We need to find x such that 3 · x ≡ 1 (mod 10)
   - Try: 3 · 1 = 3 ≠ 1
   - Try: 3 · 2 = 6 ≠ 1
   - Try: 3 · 3 = 9 ≠ 1
   - Try: 3 · 7 = 21 ≡ 1 (mod 10) ✓
   - So **3⁻¹ = 7**

3. **7**: We already found: 7 · 3 = 21 ≡ 1 (mod 10)
   - So **7⁻¹ = 3**

4. **9**: 9 · 9 = 81 ≡ 1 (mod 10)
   - So **9⁻¹ = 9** (9 is its own inverse!)

### Verification using Extended Euclidean Algorithm:

**For 3 in Z_10:**
- We want: 3x ≡ 1 (mod 10)
- This means: 3x + 10y = 1 for some integer y
- Using Extended Euclidean Algorithm:
  - 10 = 3 · 3 + 1
  - 3 = 1 · 3 + 0
  - Working backwards: 1 = 10 - 3 · 3
  - So: 1 = 10 · 1 + 3 · (-3)
  - Taking mod 10: 3 · (-3) ≡ 1 (mod 10)
  - But -3 ≡ 7 (mod 10), so: 3 · 7 ≡ 1 (mod 10) ✓

---

## How to Write Units

### Option 1: Simple List
```
Units in Z_10: {1, 3, 7, 9}
```

### Option 2: With Inverses
```
Units in Z_10: {1, 3, 7, 9}

Multiplicative inverses:
- 1⁻¹ = 1
- 3⁻¹ = 7
- 7⁻¹ = 3
- 9⁻¹ = 9
```

### Option 3: Complete Solution for Task 4
```
Units in Z_10: {1, 3, 7, 9}

These are the elements coprime to 10 (gcd(a, 10) = 1).

Inverses:
1 · 1 = 1, so 1⁻¹ = 1
3 · 7 = 21 ≡ 1 (mod 10), so 3⁻¹ = 7
7 · 3 = 21 ≡ 1 (mod 10), so 7⁻¹ = 3
9 · 9 = 81 ≡ 1 (mod 10), so 9⁻¹ = 9
```

---

## Relationship: Units vs Zero Divisors

In **Z_n**:
- **Units**: Elements with gcd(a, n) = 1 → Have inverses
- **Zero divisors**: Elements with gcd(a, n) > 1 → Cannot have inverses
- **0**: Special case, neither unit nor zero divisor

**Important**: Every nonzero element is either a **unit** or a **zero divisor**, but **never both**!

---

## Quick Examples

### Z_8:
- gcd(1, 8) = 1 → unit
- gcd(3, 8) = 1 → unit
- gcd(5, 8) = 1 → unit
- gcd(7, 8) = 1 → unit
- **Units: {1, 3, 5, 7}**

### Z_7 (prime):
- Since 7 is prime, gcd(a, 7) = 1 for all a ∈ {1, 2, 3, 4, 5, 6}
- **Units: {1, 2, 3, 4, 5, 6}** (all nonzero elements!)

### Z_15:
- **Units**: All elements coprime to 15
- Factors of 15: 3, 5
- Exclude multiples of 3 and 5
- **Units: {1, 2, 4, 7, 8, 11, 13, 14}**

---

## Summary for Your Assignment (Task 4, Part 2)

**For Z_10:**

**Units: {1, 3, 7, 9}**

These are the elements that have multiplicative inverses because gcd(a, 10) = 1.

You can write:
```
Units in Z_10: {1, 3, 7, 9}
```

Or with inverses:
```
Units in Z_10: {1, 3, 7, 9}
- 1⁻¹ = 1 (since 1 · 1 = 1)
- 3⁻¹ = 7 (since 3 · 7 = 21 ≡ 1 mod 10)
- 7⁻¹ = 3 (since 7 · 3 = 21 ≡ 1 mod 10)
- 9⁻¹ = 9 (since 9 · 9 = 81 ≡ 1 mod 10)
```


