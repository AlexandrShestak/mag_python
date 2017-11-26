import itertools


def unique(iterable):
    visited = set()
    for elem in iterable:
        if elem not in visited:
            yield elem
            visited.add(elem)


def transpose(iterable):
    return list(itertools.izip_longest(*iterable))
