import re


def index(text, numbers, k=5):
    if isinstance(numbers, int):
        numbers = (numbers,)

    positions = []
    total_occurrences = 0
    for number in numbers:
        occurrences_list = [matcher.start() + 1 for matcher in re.finditer(str(number), text)]
        total_occurrences += occurrences_list.__len__()
        positions += occurrences_list

    return total_occurrences, sorted(positions)[:k]
