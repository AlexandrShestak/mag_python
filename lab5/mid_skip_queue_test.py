import unittest
from mid_skip_queue import MidSkipQueue
from mid_skip_queue import MidSkipPriorityQueue


class TestMidSkipQueue(unittest.TestCase):
    def test_constructor(self):
        msq = MidSkipQueue(2)
        self.assertEqual(msq.container, [])

        msq = MidSkipQueue(2, [1, 2])
        self.assertEqual(msq.container, [1, 2])

        msq = MidSkipQueue(2, [1])
        self.assertEqual(msq.container, [1])

        msq = MidSkipQueue(2, [1, 2, 3])
        self.assertEqual(msq.container, [1, 2, 3])

        msq = MidSkipQueue(2, [1, 2, 3, 4, 5])
        self.assertEqual(msq.container, [1, 2, 4, 5])

        self.assertRaises(ValueError, MidSkipQueue, -1)
        self.assertRaises(ValueError, MidSkipQueue, 1.2)
        self.assertRaises(ValueError, MidSkipQueue, 'a')

    def test_len(self):
        msq = MidSkipQueue(2)
        self.assertEqual(len(msq), 0)

        msq = MidSkipQueue(2, [1, 2])
        self.assertEqual(len(msq), 2)

        msq = MidSkipQueue(2, [1, 2, 3, 4, 5, 6])
        self.assertEqual(len(msq), 4)

    def test_comparison(self):
        msq1 = MidSkipQueue(1, [2, 3, 2])
        msq2 = MidSkipQueue(1, [2, 5, 2])
        self.assertTrue(msq1 == msq2)

        msq1 = MidSkipQueue(1, [2, 3, 2])
        msq2 = MidSkipQueue(1, [2, 5, 1])
        self.assertFalse(msq1 == msq2)

    def test_get_bu_index(self):
        msq = MidSkipQueue(2, [2, 3, 4])
        self.assertRaises(AssertionError, msq.__getitem__, 100)
        self.assertRaises(AssertionError, msq.__getitem__, 's')
        self.assertRaises(AssertionError, msq.__getitem__, -4)
        self.assertEqual(msq[0], 2)
        self.assertEqual(msq[1], 3)
        self.assertEqual(msq[2], 4)
        self.assertEqual(msq[-1], 4)
        self.assertEqual(msq[-2], 3)
        self.assertEqual(msq[-3], 2)

    def test_index(self):
        msq = MidSkipQueue(2, [2, 3, 4])
        self.assertEqual(msq.index(2), 0)
        self.assertEqual(msq.index(3), 1)
        self.assertEqual(msq.index(4), 2)
        self.assertEqual(msq.index(5), -1)

    def test_contains(self):
        msq = MidSkipQueue(2, [2, 3, 4])
        self.assertTrue(msq.__contains__(2))
        self.assertTrue(msq.__contains__(4))
        self.assertFalse(msq.__contains__(5))

    def test_plus_operator(self):
        msq = MidSkipQueue(2, [2, 3, 4])
        new_msq = msq + [8, 9, 10]
        self.assertEqual(new_msq.container, [2, 3, 9, 10])
        self.assertEqual(msq.container, [2, 3, 4])

    def test_get_slice(self):
        msq = MidSkipQueue(2, [2, 3, 4])
        self.assertEqual(msq[1:3], [3, 4])

    def test_MidSkipPriorityQueue(self):
        mspq = MidSkipPriorityQueue(1)
        mspq.append(- 1)  # q : [ - 1 ]
        self.assertEqual(mspq.container, [-1])
        mspq += (-2, - 3)  # q : [ -3 , -1 ] - the smallest and the largest items
        self.assertEqual(mspq.container, [-3, -1])
        mspq.append(4)  # q : [ -3 , 4 ] - the largest item is replaced
        self.assertEqual(mspq.container, [-3, 4])
        mspq.append(- 5)  # q : [ -5 , 4 ] - the smallest item is replaced
        self.assertEqual(mspq.container, [-5, 4])


if __name__ == '__main__':
    unittest.main()
