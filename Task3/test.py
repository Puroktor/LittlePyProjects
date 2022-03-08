import unittest

from main import main


def read_all(file_name):
    with open(file_name, "r") as file:
        return file.read()


class FunctionalTest(unittest.TestCase):

    def test_main(self):
        main("01")
        self.assertEqual(read_all("tests/output01.txt"), "0.0 0.0\n5.0 5.0\n5.0 0.0\n\n----------------\n")

        main("02")
        self.assertEqual(read_all("tests/output02.txt"), "0.0 0.0\n5.0 5.0\n5.0 0.0\n\n" +
                         "0.0 0.0\n10.0 10.0\n10.0 0.0\n\n0.0 0.0\n5.0 5.0\n0.0 5.0\n\n----------------\n")

        main("03")
        self.assertEqual(read_all("tests/output03.txt"), "0.0 0.0\n5.0 5.0\n5.0 0.0\n\n" +
                         "0.0 0.0\n10.0 10.0\n10.0 0.0\n\n0.0 0.0\n5.0 5.0\n0.0 5.0\n\n----------------\n" +
                         "0.0 0.0\n2.0 3.0\n6.0 5.0\n\n----------------\n")

        main("04")
        self.assertEqual(read_all("tests/output04.txt"), "0.0 0.0\n5.0 5.0\n5.0 0.0\n\n" +
                         "0.0 0.0\n10.0 10.0\n10.0 0.0\n\n0.0 0.0\n5.0 5.0\n0.0 5.0\n\n----------------\n" +
                         "0.0 0.0\n5.0 5.0\n5.0 1.0\n\n0.0 0.0\n10.0 10.0\n10.0 2.0\n\n----------------\n" +
                         "0.0 0.0\n2.0 3.0\n6.0 5.0\n\n----------------\n")

        main("05")
        self.assertEqual(read_all("tests/output05.txt"), "0.0 0.0\n5.0 5.0\n5.0 0.0\n\n----------------\n" +
                         "0.0 0.0\n5.0 5.0\n5.0 1.0\n\n----------------\n")

        main("06")
        self.assertEqual(read_all("tests/output06.txt"), "")


if __name__ == '__main__':
    unittest.main()
