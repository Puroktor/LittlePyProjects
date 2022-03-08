def is_specific_ordered_sequence(matrix):
    if not matrix or not matrix[0]:
        return True
    increasing = decreasing = True
    h = len(matrix)
    last = matrix[0][0]
    for i in range(h):
        j_range = range(0, len(matrix[i])) if i % 2 == 0 else range(len(matrix[i]) - 1, -1, -1)
        for j in j_range:
            if matrix[i][j] < last:
                increasing = False
            elif matrix[i][j] > last:
                decreasing = False
            last = matrix[i][j]
    return increasing or decreasing


if __name__ == '__main__':
    test_matrix = [[1, 2, 3, 4], [8, 7, 6, 5], [9, 10, 11, 12]]
    print(is_specific_ordered_sequence(test_matrix))
