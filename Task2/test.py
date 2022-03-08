import unittest

from main import is_specific_ordered_sequence


class OrderTest(unittest.TestCase):

    def test_order(self):
        self.assertEqual(is_specific_ordered_sequence([]), True)
        self.assertEqual(is_specific_ordered_sequence([[1, 2, 3, 4], []]), True)
        self.assertEqual(is_specific_ordered_sequence([[1], [2], [3]]), True)
        self.assertEqual(is_specific_ordered_sequence([[], []]), True)
        self.assertEqual(is_specific_ordered_sequence([[1, 2, 3, 4], [8, 7, 6, 5], [1, 2, 3, 4]]), False)
        self.assertEqual(is_specific_ordered_sequence([[1, 2, 3, 4], [8, 7, 6, 5], [9, 10, 11, 12]]), True)
        self.assertEqual(is_specific_ordered_sequence([[12, 11, 10, 9], [5, 6, 7, 8], [4, 3, 2, 1]]), True)


if __name__ == '__main__':
    unittest.main()
