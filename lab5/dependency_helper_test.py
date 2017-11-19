import unittest
from dependency_helper import DependencyHelper


class TestMidSkipQueue(unittest.TestCase):
    def test_adding(self):
        dh = DependencyHelper()
        dh.add(1, 2)
        self.assertEqual(dh.container[1], [2])

        dh.add(1, 3)
        self.assertEqual(dh.container[1], [2, 3])

        dh.add(2, 3)
        self.assertEqual(len(dh.container), 2)

        dh += (5, 4)
        self.assertEqual(dh.container[5], [4])

    def test_remove(self):
        dh = DependencyHelper()
        dh.add(1, 2)
        dh.add(1, 3)
        self.assertEqual(dh.container[1], [2, 3])

        dh.remove((1, 2))
        self.assertEqual(dh.container[1], [3])

        dh -= (1, 3)
        self.assertEqual(dh.container[1], [])

    def test_copy(self):
        dh = DependencyHelper()
        dh.add(1, 2)
        dh.add(1, 3)

        dh_copy = dh.copy()
        self.assertEqual(dh_copy.container[1], [2, 3])

        dh.remove((1, 2))
        self.assertEqual(dh.container[1], [3])
        self.assertEqual(dh_copy.container[1], [2, 3])

    def test_get_dependent(self):
        dh = DependencyHelper()
        dh.add(1, 2)
        dh.add(1, 3)
        dh.add(3, 1)

        self.assertEqual(dh.get_dependent(1), [2, 3])

    def test_has_dependencies(self):
        dh = DependencyHelper()
        dh.add(1, 2)
        dh.add(2, 1)

        self.assertTrue(dh)

        dh = DependencyHelper()
        dh.add(1, 2)
        dh.add(2, 3)
        dh.add(3, 1)

        self.assertTrue(dh)

        dh = DependencyHelper()
        dh.add(1, 2)
        dh.add(2, 3)
        dh.add(3, 4)
        dh.add(3, 1)

        self.assertTrue(dh)

        dh = DependencyHelper()
        dh.add(1, 2)
        dh.add(2, 3)
        dh.add(3, 4)

        self.assertFalse(dh)


if __name__ == '__main__':
    unittest.main()
