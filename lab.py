# Фамилия Имя группа
import math

# Получаем от пользователя начальное и конечное значения аргумента, а также шаг разбиения
t = float(input("Введите начальное значение аргумента: "))
tn = float(input("Введите конечное значение аргумента: "))
h = float(input("Введите шаг разбиения данного отрезка: "))

# Выводим шапку таблицы
print("-" * 30)
three_space = " " * 3
print(
    "|" + three_space + "t" + three_space + "|" + three_space + "x" + " " * 5 + "|" + three_space + "y"
    + three_space * 2 + "|")
print("|" + "-" * 29)

# Основной цикл в котором мы считаем значения x и y и выводим в виде таблицы значений
while t <= tn:
    x = 2 * (math.cos(t) + t * math.sin(t))
    y = 2 * (math.sin(t) - t * math.cos(t))
    first_part_output = "|   {:1g}".format(t)
    second_part_output = "| {:g}".format(x)
    third_part_output = "| {:.5g}".format(y)
    print(first_part_output + " " * (8 - len(first_part_output)) + second_part_output + " "
          * (10 - len(second_part_output)) + third_part_output + " " * (11 - len(third_part_output)) + "|")
    t += h
print("-" * 30)
