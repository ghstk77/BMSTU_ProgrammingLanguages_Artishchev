from random import uniform
from math import isfinite

r = float(input("Введите R: "))

if not isfinite(r) or r <= 0:
    print("R должен быть конечным числом больше нуля.")
else:
    print("Десять выстрелов, вариант 1")
    print(" №       X          Y       Результат")
    for n in range(1, 11):
        x = uniform(-r, r)
        y = uniform(-r, r)
        hit = x ** 2 + y ** 2 <= r ** 2 and (
            (x >= 0 and y >= x) or (x <= 0 and y <= x)
        )
        result = "Попадание" if hit else "Промах"
        print("{:2} {:10.4f} {:10.4f}   {}".format(n, x, y, result))
