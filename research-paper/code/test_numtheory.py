import math
import random

import pytest

from numtheory import ext_gcd, gcd, modpow, sieve


def test_sieve_small_primes():
    assert sieve(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_sieve_edge_cases():
    assert sieve(1) == []
    assert sieve(2) == [2]


def test_sieve_count_below_100():
    assert len(sieve(100)) == 25


def test_gcd_matches_math_gcd_random():
    rng = random.Random(0)
    for _ in range(500):
        a = rng.randint(-10**6, 10**6)
        b = rng.randint(-10**6, 10**6)
        assert gcd(a, b) == math.gcd(a, b)


def test_ext_gcd_bezout_identity_random():
    rng = random.Random(1)
    for _ in range(500):
        a = rng.randint(-10**6, 10**6)
        b = rng.randint(-10**6, 10**6)
        d, x, y = ext_gcd(a, b)
        assert d == math.gcd(a, b)
        assert a * x + b * y == d


@pytest.mark.parametrize(
    "base, exp, mod",
    [(2, 10, 1000), (7, 128, 13), (3, 0, 7), (10, 20, 1), (123, 456, 789)],
)
def test_modpow_matches_builtin(base, exp, mod):
    assert modpow(base, exp, mod) == pow(base, exp, mod)


def test_modpow_rejects_bad_input():
    with pytest.raises(ValueError):
        modpow(2, 3, 0)
    with pytest.raises(ValueError):
        modpow(2, -1, 5)
