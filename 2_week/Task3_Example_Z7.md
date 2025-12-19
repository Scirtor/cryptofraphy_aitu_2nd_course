# Task 3: Example with Z_7

## Set of Residues Modulo 7

The **set of residues modulo 7** is all possible remainders when dividing integers by 7.

Since we require: **0 ≤ r < 7**

The residues are: **{0, 1, 2, 3, 4, 5, 6}**

This is exactly the set **Z_7** = {0, 1, 2, 3, 4, 5, 6}

---

## Addition Table for Z_7

The addition table shows the result of **(a + b) mod 7** for all a, b ∈ Z_7.

### How to read the table:
- Entry in row **a** and column **b** = **(a + b) mod 7**

### Complete Addition Table for Z_7:

```
        +  |  0   1   2   3   4   5   6
        ---|---------------------------
         0 |  0   1   2   3   4   5   6
         1 |  1   2   3   4   5   6   0
         2 |  2   3   4   5   6   0   1
         3 |  3   4   5   6   0   1   2
         4 |  4   5   6   0   1   2   3
         5 |  5   6   0   1   2   3   4
         6 |  6   0   1   2   3   4   5
```

---

## Examples:

1. **3 + 4 = ?**
   - Regular addition: 3 + 4 = 7
   - In Z_7: 7 mod 7 = **0**
   - So: **3 + 4 = 0** in Z_7

2. **5 + 6 = ?**
   - Regular addition: 5 + 6 = 11
   - In Z_7: 11 mod 7 = **4**
   - So: **5 + 6 = 4** in Z_7

3. **2 + 4 = ?**
   - Regular addition: 2 + 4 = 6
   - In Z_7: 6 mod 7 = **6**
   - So: **2 + 4 = 6** in Z_7

---

## Properties to Notice:

1. **Additive Identity**: 0 is the identity element
   - For any a: a + 0 = a

2. **Additive Inverses**: Every element has an additive inverse
   - 1 + 6 = 0, so 1⁻¹ = 6 and 6⁻¹ = 1
   - 2 + 5 = 0, so 2⁻¹ = 5 and 5⁻¹ = 2
   - 3 + 4 = 0, so 3⁻¹ = 4 and 4⁻¹ = 3
   - 0 + 0 = 0, so 0 is its own inverse

3. **Commutative**: a + b = b + a (table is symmetric)

4. **Pattern**: Notice how each row is just a cyclic shift!


