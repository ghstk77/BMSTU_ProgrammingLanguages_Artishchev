from random import uniform

n = int(input("Введите количество элементов (1 <= N <= 30): "))

if n < 1 or n > 30:
    print("Количество элементов должно быть от 1 до 30.")
else:
    a = []
    for i in range(n):
        a.append(uniform(-5, 5))
    print("Исходный массив:")
    for value in a:
        print("{:.6f}".format(value), end=" ")
    print()

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
    print("Сумма отрицательных элементов: {:.6f}".format(negative_sum))

    left = imin
    right = imax
    if left > right:
        left, right = right, left
    if right - left <= 1:
        print("Между минимумом и максимумом нет элементов.")
    else:
        product = 1
        for i in range(left + 1, right):
            product *= a[i]
        print("Произведение между минимумом и максимумом: {:.6f}".format(product))

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print("Массив по возрастанию:")
    for value in a:
        print("{:.6f}".format(value), end=" ")
    print()
