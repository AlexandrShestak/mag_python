import pprint
import copy


class MidSkipQueue(object):
    pp = pprint.PrettyPrinter()

    def __init__(self, k, iterable=[]):
        if not isinstance(k, (int, long)) or k <= 0:
            raise ValueError("k must be positive integer value")
        self.k = k
        self.container = []

        for elem in iterable:
            self.__append__(elem)

    def __str__(self):
        return self.pp.pformat(" ".join((str(x) for x in self.container)))

    def __len__(self):
        return len(self.container)

    def __eq__(self, other):
        return self.k == other.k and self.container == other.container

    def __getitem__(self, item):
        assert isinstance(item, (int, long))
        if item > 0:
            assert abs(item) < len(self)
        else:
            assert abs(item) < len(self) + 1

        return self.container[item]

    def __getslice__(self, start, end):
        return self.container.__getslice__(start, end)

    def __contains__(self, item):
        if self.container.__contains__(item):
            return True
        return False

    def index(self, elem):
        if self.container.__contains__(elem):
            return self.container.index(elem)
        return -1

    def __add__(self, iterable):
        msq = copy.deepcopy(self)
        for elem in iterable:
            msq.__append__(elem)
        return msq

    def __iadd__(self, iterable):
        return self + iterable

    def append(self, *arg):
        for elem in arg:
            self.__append__(elem)

    def __append__(self, elem):
        if len(self.container) == 2 * self.k:
            del self.container[self.k]
        self.container.append(elem)


class MidSkipPriorityQueue(MidSkipQueue):
    def __init__(self, k, iterable=[]):
        super(MidSkipPriorityQueue, self).__init__(k, iterable)
        self.k = k
        self.container = []

        elements = sorted(iterable)
        for elem in elements[0: min(len(elements), self.k)]:
            self.__append__(elem)

        if len(elements) > self.k:
            for elem in elements[(len(elements) - self.k) * -1:]:
                self.__append__(elem)

    def __append__(self, elem):
        if len(self.container) == 2 * self.k:
            if elem < min(self.container[0: self.k]):
                self.container[self.k - 1] = elem
            else:
                min_second_part_elem = min(self.container[self.k: 2 * self.k])
                min_second_part_elem_index = self.k + self.container[self.k: 2 * self.k].index(min_second_part_elem)
                self.container[min_second_part_elem_index] = elem
        else:
            self.container.append(elem)

    def __add__(self, iterable):
        return MidSkipPriorityQueue(self.k, self.container + list(iterable))

    def __iadd__(self, iterable):
        return self + iterable
