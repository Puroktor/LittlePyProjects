import unittest
import codecs

from main import main


def read_all(file_name):
    with codecs.open(file_name, 'r', encoding='utf-8') as file:
        return file.read()


class FunctionalTest(unittest.TestCase):

    def test_main(self):
        main("01")
        self.assertEqual(read_all("tests/output01.txt"), "Иванов Иван Иванович\nАлгазинов Э.К.\n")

        main("02")
        self.assertEqual(read_all("tests/output02.txt"), "")

        main("03")
        self.assertEqual(read_all("tests/output03.txt"), "Ововыио А.В.\n")

        main("04")
        self.assertEqual(read_all("tests/output04.txt"), "Ав Ав Ва\n")

        main("05")
        self.assertEqual(read_all("tests/output05.txt"), "")

        main("06")
        self.assertEqual(read_all("tests/output06.txt"), "")


if __name__ == '__main__':
    unittest.main()
