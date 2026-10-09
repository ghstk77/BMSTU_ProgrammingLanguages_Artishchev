import turtle as tr
from random import uniform
from math import pi, isfinite


def is_hit(x, y, r):
    return x ** 2 + y ** 2 <= r ** 2 and (
        (x >= 0 and y >= x) or (x <= 0 and y <= x)
    )


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


if __name__ == "__main__":
    r = float(input("Введите R: "))
    n = int(input("Введите число испытаний (1 <= N <= 10000): "))
    if not isfinite(r) or r <= 0 or not 1 <= n <= 10000:
        raise ValueError("Нужно R > 0 и от 1 до 10000 испытаний.")
    screen = tr.Screen()
    screen.setup(width=0.9, height=0.8)
    screen.title("Лабораторная работа 7. Метод Монте-Карло, вариант 1")
    ratio = screen.window_width() / screen.window_height()
    xlim = 1.3 * r * max(1, ratio)
    ylim = 1.3 * r * max(1, 1 / ratio)
    screen.setworldcoordinates(-xlim, -ylim, xlim, ylim)
    tr.hideturtle()
    tr.tracer(0)
    hits = 0
    tr.penup()
    for i in range(n):
        x = uniform(-r, r)
        y = uniform(-r, r)
        hit = is_hit(x, y, r)
        if hit:
            hits += 1
        tr.goto(x, y)
        tr.dot(2, "green" if hit else "lightgray")
    tr.color("black")
    draw_axes(-xlim * 0.9, xlim * 0.9, -ylim * 0.9, ylim * 0.9)
    area = 4 * r ** 2 * hits / n
    real_area = pi * r ** 2 / 4
    error = abs(area - real_area) / real_area * 100
    result = "N = {}, попаданий = {}, S = {:.6g}, точная S = {:.6g}, ошибка = {:.2f}%".format(
        n, hits, area, real_area, error
    )
    print(result)
    tr.penup()
    labels = ["N = {}, попаданий = {}".format(n, hits),
              "S = {:.6g}, точная S = {:.6g}".format(area, real_area),
              "Относительная ошибка = {:.2f}%".format(error)]
    for i, label in enumerate(labels):
        tr.goto(-xlim * 0.94, ylim * (0.94 - i * 0.08))
        tr.write(label, align="left", font=("Arial", 10, "normal"))
    tr.goto(0, -ylim * 0.92)
    tr.write("Зелёный — попадание; серый — промах", align="center")
    tr.update()
    tr.done()
