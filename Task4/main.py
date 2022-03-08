import re
import codecs


def find_names(file_name):
    names = []
    with codecs.open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            names.extend(re.findall('[А-Я][а-я]+ [А-Я][а-я]+ [А-Я][а-я]+', line))
            names.extend(re.findall('[А-Я][а-я]+ [А-Я]\.[А-Я]\.', line))
    return names


def write_array(file_name, arr):
    with codecs.open(file_name, 'w', encoding='utf-8') as file:
        file.writelines('%s\n' % elem for elem in arr)


def main(number):
    names = find_names('tests/input%s.txt' % number)
    write_array('tests/output%s.txt' % number, names)


if __name__ == '__main__':
    main("06")
