from pathlib import Path

folder = Path(__file__).parent
with open(folder / "input_04.txt", encoding="utf-8") as source:
    n = int(source.readline())
    a = list(map(float, source.read().split()))
if not 1 <= n <= 30 or len(a) != n:
    raise ValueError("Нужно от 1 до 30 элементов, их количество должно совпадать с N.")

with open(folder / "output_04.txt", "w", encoding="utf-8") as result:
    print("Исходный массив:", file=result)
    for value in a:
        print("{:.6f}".format(value), end=" ", file=result)
    print(file=result)

    negative_sum = 0
    imin = 0
    imax = 0
    for i in range(n):
        if a[i] < 0:
            negative_sum += a[i]
        if a[i] < a[imin]:
            imin = i
        if a[i] > a[imax]:
            imax = i
    print("Сумма отрицательных элементов: {:.6f}".format(negative_sum), file=result)

    left = imin
    right = imax
    if left > right:
        left, right = right, left
    if right - left <= 1:
        print("Между минимумом и максимумом нет элементов.", file=result)
    else:
        product = 1
        for i in range(left + 1, right):
            product *= a[i]
        print("Произведение между минимумом и максимумом: {:.6f}".format(product), file=result)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print("Массив по возрастанию:", file=result)
    for value in a:
        print("{:.6f}".format(value), end=" ", file=result)
    print(file=result)
