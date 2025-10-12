flag = False
print('Введите координаты X и Y для точки:')
x = float(input('X='))
y = float(input('Y='))

if (-1 <= x < 1) and (2*x+2 <= y <= x**3-4*x**2+x+6) \
        or (1 <= x <= 4) and (x**3-4*x**2+x+6 <= y <= 2*x+2):
    flag = True
else:
    flag = False

print("Точка X={0: 6.2f} Y={1: 6.2f}".format(x, y), end=" ")
if flag:
    print("попадает", end=" ")
else:
    print("не попадает", end=" ")
print("в область.")
