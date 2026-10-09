from pathlib import Path

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


folder = Path(__file__).parent
with open(folder / "input_05.txt", encoding="utf-8") as source:
    rows, cols = map(int, source.readline().split())
    matrix = [list(map(int, line.split())) for line in source]
if rows <= 0 or cols <= 0 or len(matrix) != rows:
    raise ValueError("Неверное количество строк или столбцов.")
for row in matrix:
    if len(row) != cols:
        raise ValueError("Длина строки не совпадает с количеством столбцов.")

with open(folder / "output_05.txt", "w", encoding="utf-8") as result:
    print("Исходная матрица:", file=result)
    for row in matrix:
        for value in row:
            print("{:6}".format(value), end=" ", file=result)
        print(file=result)
    print("Строк без нулей:", count_nonzero_rows(matrix), file=result)
    repeated = max_repeated_value(matrix)
    if repeated is None:
        print("Повторяющихся чисел нет.", file=result)
    else:
        print("Максимальное повторяющееся число:", repeated, file=result)
