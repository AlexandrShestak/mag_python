def sum_digits(number):
    number_sum = 0
    while number:
        number_sum += number % 10
        number //= 10
    return number_sum


def happy_number(number):
    first_part = str(number)[0:3]
    second_part = str(number)[3:6]
    return sum_digits(int(first_part)) == sum_digits(int(second_part))


def is_lucky_ticket(number):
    nearest_higher = number
    nearest_lower = 0

    for x in xrange(number, 1000000):
        if happy_number(x):
            nearest_higher = x
            break

    for x in xrange(number, 100000, -1):
        if happy_number(x):
            nearest_lower = x
            break

    return nearest_higher if (nearest_higher - number < number - nearest_lower) else nearest_lower
