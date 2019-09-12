# Gram-Schmidt / LLL

Sage wouldn't start up for me one day and the one Gram-Schmidt orthogonalization calculator I could find online was being extremely slow due to poor Wi-Fi, so I decided to write up my own implementation of the algorithm using a custom defined Vector class similar to the one used by Sage (albeit skeletonized).  I also recently added an implementation for the Lenstra–Lenstra–Lovász (LLL) lattice basis reduction algorithm, which takes a lattice (discrete additive subgroup of R^n) basis and generates from it a basis with shorter, nearly orthogonal vectors.  LLL is used in many cryptanalytical attacks against cryptosystems such as RSA, and I intend to implement some more of these attacks (in [RSA Attacks](https://github.com/pwang00/RSA-Attacks.git)) from scratch using this repository as proof-of-concept.  

Disclaimers: most of the code here is unoptimized and pretty clunky as of yet, so I'll spend some time sometime and clean it up.

# Requirements

* Python 3.x

# Usage

The following are examples denoting usages of the gram_schmidt class:
```python
from gram_schmidt import *
from vector import Vector
    
v1 = Vector([1, 0, 0, 1])
v2 = Vector([-1, 0, 2, 1])
v3 = Vector([0, 1, 2, 0])
v4 = Vector([0, 0, -1, 1])
```
The below two expressions are equivalent:
```python
result1 = gram_schmidt(v1, v2, v3, v4)
result2 = gram_schmidt([v1, v2, v3, v4])
assert result1 == result2
```

The ```normalize``` flag causes gram_schmidt() to return an orthonormal set of vectors (such that magnitude v for v in vectors = 1) with floating point components (currently needs bug fixing)

```python
result1 = gram_schmidt([v1, v2, v3, v4], normalize=True)
result2 = gram_schmidt(v1, v2, v3, v4, normalize=True)
assert result1 == result2
```
The ```fraction``` flag causes gram_schmidt() to return a set of vectors with fraction components (if the vector components are not already integers) as to improve readability (considering improving representation of fractions atm).

```python
result1 = gram_schmidt([v1, v2, v3, v4], fraction=True)
result2 = gram_schmidt(v1, v2, v3, v4, fraction=True)
assert result1 == result2

# Prints result
print(result1)
```

The usage of LLL is very similar to that of Gram-Schmidt, as shown below:

```python
l_basis = [vector((3, 4, 5)), vector((6, 7, 8)), vector((9, 10, 11))]

result = LLL(l_basis, d=0.75)
print(result)

# [(0, 0, 0), (0, -1, -2), (3, 1, -1)]
```

Note that the input vectors are the column space of a lattice, not row space.  I should consider adding a matrix class with transposition support to better complement LLL.

# TODO

* Add tests and apply necessary bug fixes
* Write a better README
* Optimize LLL so that it doesn't gram_schmidt every time a vector is changed









