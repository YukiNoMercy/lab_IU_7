# Фамилия Имя группа
import math

# Получаем от пользователя начальное и конечное значения аргумента, а также шаг разбиения
t = float(input("Введите начальное значение аргумента: "))
tn = float(input("Введите конечное значение аргумента: "))
h = float(input("Введите шаг разбиения данного отрезка: "))
# Сохраняем начальное значение параметра в отдельную переменную
temp = t
# создаём переменную для хранения информации о том пересекает ли функция 0
flag = False
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
    if y == 0:
        flag = True
    t += h
print("-" * 30)

serifs = int(input("Введите колличество засечек (от 4 до 8): "))
# Обнуляем значение переменной t
t = temp
weigh = 90
max_y = 0
min_y = 0
# Ищем минимальное и максимальное значения, которые принимает функция
while t <= tn:
    y = 2 * (math.sin(t) - t * math.cos(t))
    if y > max_y:
        max_y = y
    if y < min_y:
        min_y = y
    t += h
# Создание и вывод масштабной линейки
first_output_graphic = " " * 5 + str(min_y) + " " * 5
count = 1
step_first_output = (max_y - min_y) / serifs
while count < serifs:
    first_output_graphic += ("{:5g}".format(min_y + step_first_output * count) + " " * 5)
    count += 1
first_output_graphic += "{:5g}".format(max_y)
print(first_output_graphic)

step_graphic = round((max_y - min_y) / len(first_output_graphic), 5)
# Обнуление параметра и создание и вывод графика
t = temp
while t <= tn:
    y = 2 * (math.sin(t) - t * math.cos(t))
    begin_string = "{:<1g}".format(t)
    begin_string += (" " * (4 - len(begin_string)) + "|")
    point = int((y - min_y) / step_graphic)
    end_string = begin_string + " " * point + "*"
    end_string += (" " * (weigh - len(end_string)))
    # Создание асимптоты
    if flag:
        end_string = end_string[:int(min_y * (-1) / step_graphic) + len(begin_string)] + "|" + end_string[
            int(min_y * (-1) / step_graphic) + 1 + len(begin_string):]
    print(end_string)
    t += h
