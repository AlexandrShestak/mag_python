from collections import defaultdict


def get_unique(collection):
    unique = defaultdict(int)
    for it in collection:
        unique[it] += 1

    return unique.items()
