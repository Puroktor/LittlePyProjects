import unittest

from main import reverse_btw_max_and_min


class TestReverse(unittest.TestCase):

    def test_reverse(self):
        test_list = []
        reverse_btw_max_and_min(test_list)
        self.assertEqual(test_list, [])

        test_list = [1, 2]
        reverse_btw_max_and_min(test_list)
        self.assertEqual(test_list, [1, 2])

        test_list = [1, 1]
        reverse_btw_max_and_min(test_list)
        self.assertEqual(test_list, [1, 1])

        test_list = [1, 1, 2]
        reverse_btw_max_and_min(test_list)
        self.assertEqual(test_list, [1, 1, 2])

        test_list = [1, 2, 3, 4]
        reverse_btw_max_and_min(test_list)
        self.assertEqual(test_list, [1, 3, 2, 4])

        test_list = [2, 11, 8, 11, 2, 3, 2, 2, 6, 7, 2, 3, 5, 10]
        reverse_btw_max_and_min(test_list)
        self.assertEqual(test_list, [2, 11, 7, 6, 2, 2, 3, 2, 11, 8, 2, 3, 5, 10])


if __name__ == '__main__':
    unittest.main()
