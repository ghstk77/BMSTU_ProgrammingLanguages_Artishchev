from math import sqrt

x = float(input("Введите значение X = "))
y = 0.0

if x < -5:
    y = 1
elif -5 <= x < 0:
    y = -(3/5)*x-2
elif 0 <= x < 2:
    y = -sqrt(4-x**2)
elif 2 <= x < 4:
    y = x - 2
elif 4 <= x < 8:
    y = 2+sqrt(4-(x-6)**2)
elif x >= 8:
    y = 2

print("X = {0:.2f} Y = {1:.2f}".format(x, y))
