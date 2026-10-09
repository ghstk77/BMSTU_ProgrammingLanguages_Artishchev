from math import sqrt, isfinite

xb = float(input("Введите Xнач: "))
xe = float(input("Введите Xкон: "))
dx = float(input("Введите шаг dx: "))

if not all(isfinite(v) for v in (xb, xe, dx)) or not -9 <= xb <= xe <= 9 or dx <= 0:
    print("Нужно -9 <= Xнач <= Xкон <= 9 и dx > 0; числа должны быть конечными.")
else:
    print("Таблица значений функции, вариант 1")
    print("Xнач = {}, Xкон = {}, dx = {}".format(xb, xe, dx))
    print("+------------+------------+")
    print("|     X      |     Y      |")
    print("+------------+------------+")
    i = 0
    x = xb
    while x <= xe or abs(x - xe) <= dx * 1e-9:
        if x > xe:
            x = xe
        if x <= -6:
            y = -sqrt(9 - (x + 6) ** 2)
        elif x <= -3:
            y = x + 3
        elif x <= 0:
            y = sqrt(9 - x ** 2)
        elif x <= 3:
            y = 3 - x
        else:
            y = (x - 3) / 2
        print("|{:12.4f}|{:12.4f}|".format(x, y))
        i += 1
        x = xb + i * dx
    print("+------------+------------+")
