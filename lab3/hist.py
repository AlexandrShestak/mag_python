def distribute(collection, n):
    max_element = max(collection)
    min_element = min(collection)
    delta = (max_element - min_element) / float(n)

    histogram = [0] * n
    for element in collection:
        if element == max_element:
            histogram[-1] += 1
        else:
            histogram[int((element - min_element) // delta)] += 1

    for elem in histogram:
        print format('', '*>%s' % elem)

    return histogram
