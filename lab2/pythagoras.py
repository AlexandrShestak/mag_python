import math


def get_pythagoras_triples(n):
    return [(x, y, z) for x in xrange(1, n + 1) for y in xrange(x, n + 1)
            for z in xrange(int(math.sqrt(x ** 2 + y ** 2)), n + 1) if z ** 2 == x ** 2 + y ** 2]

