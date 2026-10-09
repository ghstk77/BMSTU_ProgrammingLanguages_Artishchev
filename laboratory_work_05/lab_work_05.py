def count_nonzero_rows(matrix):
    count = 0
    for row in matrix:
        has_zero = False
        for value in row:
            if value == 0:
                has_zero = True
                break
        if not has_zero:
            count += 1
    return count


def max_repeated_value(matrix):
    counts = {}
    for row in matrix:
        for value in row:
            if value in counts:
                counts[value] += 1
            else:
                counts[value] = 1
    result = None
    for value in counts:
        if counts[value] > 1 and (result is None or value > result):
            result = value
    return result


rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

if rows <= 0 or cols <= 0:
    print("Размеры матрицы должны быть положительными.")
else:
    matrix = []
    for i in range(rows):
        row = list(map(int, input("Строка {} ({} целых чисел): ".format(i + 1, cols)).split()))
        while len(row) != cols:
            row = list(map(int, input("Введите ровно {} целых чисел: ".format(cols)).split()))
        matrix.append(row)

    print("Исходная матрица:")
    for row in matrix:
        for value in row:
            print("{:6}".format(value), end=" ")
        print()
    print("Строк без нулей:", count_nonzero_rows(matrix))
    result = max_repeated_value(matrix)
    if result is None:
        print("Повторяющихся чисел нет.")
    else:
        print("Максимальное повторяющееся число:", result)
