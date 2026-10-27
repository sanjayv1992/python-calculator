"""Elementary number theory routines used in the research paper.

Each function corresponds to a result in the paper; see the chapter
references in the docstrings.
"""


def sieve(n: int) -> list[int]:
    """Return all primes less than or equal to n (Sieve of Eratosthenes)."""
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
        p += 1
    return [i for i, flag in enumerate(is_prime) if flag]


def gcd(a: int, b: int) -> int:
    """Greatest common divisor by the Euclidean algorithm (Theorem 2.3)."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def ext_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Return (d, x, y) with a*x + b*y = d = gcd(a, b) (Theorem 2.4)."""
    old_r, r = a, b
    old_x, x = 1, 0
    old_y, y = 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_x, x = x, old_x - q * x
        old_y, y = y, old_y - q * y
    if old_r < 0:
        return -old_r, -old_x, -old_y
    return old_r, old_x, old_y


def phi(n: int) -> int:
    """Euler's totient: count of 1 <= k <= n with gcd(k, n) = 1 (Chapter 4)."""
    if n < 1:
        raise ValueError("n must be positive")
    result = n
    m = n
    p = 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            result -= result // p
        p += 1
    if m > 1:
        result -= result // m
    return result


def modpow(base: int, exp: int, mod: int) -> int:
    """Compute base**exp mod mod by repeated squaring (used in Chapter 4)."""
    if mod <= 0:
        raise ValueError("modulus must be positive")
    if exp < 0:
        raise ValueError("exponent must be non-negative")
    result = 1 % mod
    base %= mod
    while exp:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result
