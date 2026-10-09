import turtle as tr
from math import isfinite


def draw_axes(xmin, xmax, ymin, ymax):
    xzero = 0 if xmin <= 0 <= xmax else xmin + (xmax - xmin) * 0.07
    yzero = 0 if ymin <= 0 <= ymax else ymin + (ymax - ymin) * 0.07
    tr.penup()
    tr.goto(xmin, yzero)
    tr.pendown()
    tr.goto(xmax, yzero)
    tr.penup()
    tr.goto(xzero, ymin)
    tr.pendown()
    tr.goto(xzero, ymax)
    tr.penup()
    tr.goto(xmax, yzero)
    tr.write("X", font=("Arial", 12, "bold"))
    tr.goto(xzero, ymax)
    tr.write("Y", font=("Arial", 12, "bold"))
    for i in range(6):
        x = xmin + (xmax - xmin) * i / 5
        y = ymin + (ymax - ymin) * i / 5
        tr.goto(x, yzero)
        tr.pendown()
        tr.goto(x, yzero - (ymax - ymin) * 0.015)
        tr.penup()
        tr.goto(x, yzero - (ymax - ymin) * 0.04)
        tr.write("{:.6g}".format(x), align="center")
        tr.goto(xzero, y)
        tr.pendown()
        tr.goto(xzero - (xmax - xmin) * 0.01, y)
        tr.penup()
        tr.write("{:.6g}".format(y), align="right")


def plot(xs, ys, title):
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    xspan = xmax - xmin if xmax > xmin else 2
    yspan = ymax - ymin if ymax > ymin else 2
    xmin -= xspan * 0.15
    xmax += xspan * 0.15
    ymin -= yspan * 0.15
    ymax += yspan * 0.15
    screen = tr.Screen()
    screen.setup(width=0.9, height=0.8)
    screen.title(title)
    screen.setworldcoordinates(xmin, ymin, xmax, ymax)
    tr.hideturtle()
    tr.tracer(0)
    draw_axes(xmin + xspan * 0.03, xmax - xspan * 0.06,
              ymin + yspan * 0.03, ymax - yspan * 0.06)
    tr.penup()
    tr.color("green")
    tr.width(2)
    tr.goto(xs[0], ys[0])
    tr.pendown()
    for x, y in zip(xs, ys):
        tr.goto(x, y)
    if len(xs) == 1:
        tr.dot(5)
    tr.update()
    tr.done()


def function(x, eps=0.001):
    term = 2 / x
    y = term
    n = 1
    q = (1 / x) ** 2
    next_term = term * q * (2 * n - 1) / (2 * n + 1)
    while abs(next_term) / (1 - q) > eps:
        y += next_term
        term = next_term
        n += 1
        next_term = term * q * (2 * n - 1) / (2 * n + 1)
    return y


if __name__ == "__main__":
    xb = float(input("Введите Xнач: "))
    xe = float(input("Введите Xкон: "))
    dx = float(input("Введите шаг dx: "))
    if not all(isfinite(v) for v in (xb, xe, dx)) or dx <= 0 or xb > xe:
        raise ValueError("Нужно Xнач <= Xкон и dx > 0; числа должны быть конечными.")
    if not (xe < -1 or xb > 1):
        raise ValueError("Отрезок должен находиться в X < -1 или X > 1.")
    xs = []
    ys = []
    i = 0
    x = xb
    while x <= xe or abs(x - xe) <= dx * 1e-9:
        if x > xe:
            x = xe
        xs.append(x)
        ys.append(function(x))
        i += 1
        x = xb + i * dx
    plot(xs, ys, "Лабораторная работа 7. Логарифмический ряд, epsilon = 0.001")
