from math import sqrt, isfinite

x = float(input("Введите X (-9 <= X <= 9): "))

if not isfinite(x) or x < -9 or x > 9:
    print("X должен принадлежать отрезку [-9; 9].")
else:
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
    print("X = {:.4f}, Y = {:.4f}".format(x, y))
