from math import isfinite

x = float(input("Введите X: "))
y = float(input("Введите Y: "))
r = float(input("Введите R: "))

if not isfinite(x) or not isfinite(y) or not isfinite(r) or r <= 0:
    print("Координаты должны быть конечными числами, R должен быть больше нуля.")
elif x ** 2 + y ** 2 <= r ** 2 and (
    (x >= 0 and y >= x) or (x <= 0 and y <= x)
):
    print("Точка попадает в область.")
else:
    print("Точка не попадает в область.")
