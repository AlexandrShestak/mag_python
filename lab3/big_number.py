import re


def index(text, numbers, k=5):
    if isinstance(numbers, int):
        numbers = (numbers,)

    positions = set()
    total_occurrences = 0
    for number in numbers:
        occurrences_set = set([matcher.start() + 1 for matcher in re.finditer(str(number), text)])
        total_occurrences += occurrences_set.__len__()
        positions.update(occurrences_set)

    return total_occurrences, sorted(positions)[:k]
