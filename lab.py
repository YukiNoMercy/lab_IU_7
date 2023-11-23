# Фамилия Имя группа
import math

print("-" * 28)
three_space = " " * 3
print(
    "|" + three_space + "t" + three_space + "|" + three_space + "x" + three_space + "|" + three_space + "y"
    + three_space * 2 + "|")
print("|" + "-" * 27)

t = 0
h = 0.3
tn = 2 * math.pi

while t <= tn:
    x = 2 * (math.cos(t) + t * math.sin(t))
    y = 2 * (math.sin(t) - t * math.cos(t))
    print("|   {:1g} | {:g}, ".format(t, x, y))
    t += h
