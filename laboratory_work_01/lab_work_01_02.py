from math import sin, cos, pi

alpha = float(input("Введите alpha в радианах: "))

z1 = 2 * sin(3 * pi - 2 * alpha) ** 2 * cos(5 * pi + 2 * alpha) ** 2
z2 = 1 / 4 - 1 / 4 * sin(5 * pi / 2 - 8 * alpha)

print("z1 = {:.10f}".format(z1))
print("z2 = {:.10f}".format(z2))
