from math import sin, cos, pi
from pathlib import Path

folder = Path(__file__).parent
with open(folder / "input.txt", encoding="utf-8") as source, \
        open(folder / "output.txt", "w", encoding="utf-8") as result:
    result.write("      alpha              z1              z2\n")
    for line in source:
        alpha = float(line)
        z1 = 2 * sin(3 * pi - 2 * alpha) ** 2 * cos(5 * pi + 2 * alpha) ** 2
        z2 = 1 / 4 - 1 / 4 * sin(5 * pi / 2 - 8 * alpha)
        result.write("{:12.6f} {:15.10f} {:15.10f}\n".format(alpha, z1, z2))
