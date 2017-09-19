from collections import defaultdict
from itertools import combinations


def get_unique(collection):
    unique = defaultdict(int)
    for it in combinations(collection, 2):
        unique[tuple(sorted(it))] += 1

    for key, value in unique.iteritems():
        print str(key) + '   ' + str(value)

    return unique


print get_unique([2, 5, 7, 3, 5, 3])
