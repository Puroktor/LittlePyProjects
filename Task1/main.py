def reverse_btw_max_and_min(numbers):
    if not numbers:
        return
    i_max = numbers.index(max(numbers))
    i_min = len(numbers) - numbers[::-1].index(min(numbers)) - 1
    if i_min > i_max:
        i_min, i_max = i_max + 1, i_min
    else:
        i_min += 1
    numbers[i_min:i_max] = numbers[i_min:i_max][::-1]


if __name__ == '__main__':
    test_list = [2, 11, 8, 11, 2, 3, 2, 2, 6, 7, 2, 3, 5, 10]
    reverse_btw_max_and_min(test_list)
    print(test_list)
