import prime_numbers

def test_lower_primes(capsys):
    # Test positive numbers
    prime_numbers.lower_primes(10)
    assert prime_numbers.lower_primes(5) == ([2, 3, 5])
    assert prime_numbers.lower_primes(41) == ([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41])

    # Test negative numbers
    assert prime_numbers.lower_primes(-10) == -1


def test_prime():
    assert prime_numbers.prime(7) == True
    assert prime_numbers.prime(13) == True
    assert prime_numbers.prime(-7) == False
    assert prime_numbers.prime(1) == False
