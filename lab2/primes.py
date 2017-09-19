def get_primes(n):
    return [x for x in xrange(1, n + 1) if all(x % i for i in xrange(2, x))]
