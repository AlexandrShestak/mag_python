def get_sequence_item(k):
    result = 0
    mask = 1
    current_result_length = 1
    for x in xrange(1, k):
        y = result ^ mask
        result = int(('{0:0%db}' % current_result_length).format(result)
                     + ('{0:0%db}' % current_result_length).format(y), 2)
        current_result_length = current_result_length << 1
        mask = (1 << current_result_length) - 1
    return result
