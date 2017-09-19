from collections import defaultdict
from itertools import combinations


def get_unique(collection):
    unique = defaultdict(int)
    for it in combinations(collection, 2):
        unique[tuple(sorted(it))] += 1

    return unique
