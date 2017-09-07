def set_bit(number, k):
    return number | 1 << k


def clear_bit(number, k):
    return number & (~(1 << k))


def test_bit(number, k):
    return bool(number & 1 << k)