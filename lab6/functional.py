import collections
import unittest
import os


def convert_value(val):
    if not isinstance(val, (int, long, float)):
        if val.startswith('0b'):
            val = int(val, 2)
        elif val.startswith('0o'):
            val = int(val, 8)
        elif val.startswith('0x'):
            val = int(val, 16)
        else:
            val = int(val)
    return val


def multiply_operator(val1, val2):
    val1 = convert_value(val1)
    val2 = convert_value(val2)
    return val1 * val2


def scalar_product(iterable1, iterable2):
    try:
        return sum(map(multiply_operator, iterable1, iterable2))
    except ValueError:
        return None


def flatten(iterable):
    for elem in iterable:
        if isinstance(elem, collections.Iterable) and not isinstance(elem, basestring):
            for sub in flatten(elem):
                yield sub
        else:
            yield elem


#
# class UnitTest(unittest.TestCase):
#     def test_flatten(self):
#         expected = [1, 2, 0, 1, 1, 3, 2, 1, 'ab']
#         actual = flatten([1, 2, xrange(2), [[], [[1, 3]], [[2]]], (x for x in [1]), 'ab'])
#
#         self.assertEqual(expected, list(actual))
#
#
# if __name__ == '__main__':
#     unittest.main()



def walk_files(path):
    map = {}
    for root, subdirs, files in os.walk(path):
        if root not in map:
            map[root] = []
        for file_name in files:
            map[root].append(file_name)
        for subdir in subdirs:
            map[root].append(walk_files(root + os.sep + subdir))
    return map


def dic_values(d):
    items = set()
    for dir_name, dir_inner_elem in d.iteritems():
        if isinstance(dir_inner_elem, dict):
            items.update(dic_values(dir_inner_elem))
        else:
            items.update(dir_name + os.sep + filename for filename in dir_inner_elem)
    return items


print list(flatten(dic_values(walk_files('/bin'))))
