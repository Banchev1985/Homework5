# проверка на смену класса
import math
from math import pi

old_list = ['1', '2', '3', '4', '5', '6', '7']
new_list_1 = list(map(int, old_list))
# print(new_list_1)
# print(type(new_list_1[0]))
assert type(new_list_1[0]) == int

# проверка на суммирование списков, через смену класса
list_1_1 = [1, 2, 3]
list_1_2 = [4, 5, 6]
new_list_2 = list(map(lambda x, y: x + y, list_1_1, list_1_2))
# print(new_list)
assert new_list_2 == [5, 7, 9]

names = ['Женя', 'Костя', 'Витя', 'Коля', 'Женя', 'Дима', 'Женя', 'Федя', 'Коля', 'Максим']
filter_names = list(filter(lambda x: x == 'Женя', names))
assert filter_names == ['Женя', 'Женя', 'Женя']
# print(filter_names)

num_list = [1, 3, 2, 5, 4, 6, 8, 7, 9, ]
num_list.sort()
assert num_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def cycle(rad):
    circumference = 2 * pi * rad
    return circumference


# print(cycle(2))
assert cycle(2) == 12.566370614359172
assert math.pi == 3.141592653589793


# print(math.pi)

def square_root(num):
    answer = math.sqrt(num)
    return answer


assert math.sqrt(100) == 10
assert square_root(100) == 10


assert math.pow(2, 2) == 4


assert math.hypot(2, 100) == 100.0199980003999
