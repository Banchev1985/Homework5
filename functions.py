import os
import platform
import sys
import shutil

# directory_path = input('Введите путь где вы хотите создать папку\название папки ')

# функция создания папки
from os.path import isdir


def decor(f):
    def inner(*args, **kwargs):
        print('$' * 3, 'Слушаюсь мой Господин', '$' * 3)
        result = f(*args, **kwargs)
        return result
    return inner


@decor
def new_directory():
    directory_name = input('Напишите имя папки ')
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
    else:
        print('Такая папка существует, введите другое имя ')


# функция удаления файла/папки
@decor
def del_file():
    file_name = input('Введите имя файла ')
    os.remove(f'{file_name}')


# Удаление папки
@decor
def del_dir():
    dir_name = input('Введите имя папки ')
    os.rmdir(f'{dir_name}')
    print('Папка удалена')


# копировать файл
@decor
def copy_file():
    old_file = input('Введите имя копируемого файла ')
    new_file = input('Введите новое имя файла ')
    shutil.copy(f'{old_file}', f'{new_file}')


@decor
def copy_directory():
    old_directory = input('Введите имя копируемой папки ')
    new_directory = input('Введите новое имя папки ')
    shutil.copytree(f'{old_directory}', f'{new_directory}')


# просмотр содержимого директории
@decor
def show_directory():
    arr = os.listdir('.')
    print(arr)


# Запись содержимого директории в файл
@decor
def write_directory():
    arr = os.listdir('.')
    files = filter(lambda x: os.path.isfile(x), arr)
    dirs = filter(lambda x: os.path.isdir(x), arr)
    with open('listdir.txt', 'w') as f:
        f.write('files: ')
        for file in files:
            f.write(f'{file}, ')
        f.write('\n')
        f.write('dirs: ')
        for dir in dirs:
            f.write(f'{dir}, ')


@decor
def system_info():
    print(platform.platform())


# показать только папки
@decor
def dir_info():
    dir_only = [item for item in os.listdir('.') if os.path.isdir(item)]
    print(list(dir_only))

    # all_objects = os.listdir()
    # dirs_only = []
    # for item in all_objects:
    #     if os.path.isdir(item):
    #         dirs_only.append(item)
    #         print(dirs_only)


# показать только файлы
@decor
def file_info():
    file_only = [item for item in os.listdir('.') if os.path.isfile(item)]
    print(list(file_only))

    # all_objects = os.listdir()
    # for item in all_objects:
    #     if os.path.isfile(item):
    #         file_only.append(item)
    #         print(file_only)


# noinspection PyBroadException
@decor
def balance():
    score = 0
    purchase = []

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
    # noinspection PyBroadException

        choice = int(input('Выберите пункт меню '))

        if choice == 1:
            score = int(input('На сколько пополнить счет? '))
            print(score)

        elif choice == 2:
            purchase_question_score = int(input('На какую суммы Вы хотите сделать покупку? '))
            (print('У Вас недостаточно средств на счете') if score < purchase_question_score else print('Приятных вам '
                                                                                                        'покупок'))
            purchase_question = str(input('Что вы хотите купить? '))
            purchase.append(purchase_question)
            score_new = score - purchase_question_score
            print(purchase)
            print(score_new)
        elif choice == 3:
            print('Вы купили', purchase)
        elif choice == 4:
            break
        else:
            print('Неверный пункт меню')




# Викторина
@decor
def victory():
    import random

    correct = 0
    incorrect = 0

    again = str(input('Хотитет поиграть? ' 'Да / Нет '))
    print('Чтобы остановить игру пишите ''стоп''')
    while again.title() == 'Да' and 'Да' or 'да' in again:

        dates = {
            'Гагарин': '09.03.1934',
            'Нагиев': '04.04.1967',
            'Путин': '07.10.1952',
            'Тесла': '10.07.1856',
            'Эйнштейн': '14.03.1879',
            'Соловьев': '20.10.1963',
            'Киркоров': '30.04.1967',
            'Ломоносов': '19.11.1711',
            'Капица': '08.07.1894',
            'Курчатов': '12.01.1903'
        }
        dates_words = {
            'Гагарин': 'девятое марта 1934 года',
            'Нагиев': 'четвертое апреля 1967 года',
            'Путин': 'седьмое октября 1952 года',
            'Тесла': 'десятое июля 1856 года',
            'Эйнштейн': 'четырнадцатое марта 1879 года',
            'Соловьев': 'двадцатое октября 1963 года',
            'Киркоров': 'тридцатое апреля 1967 года',
            'Ломоносов': 'девятнадцатое ноября 1711 года',
            'Капица': ' восьмое июня 1894 года',
            'Курчатов': 'двенадцатое января 1903 года'
        }

        names_list = ('Гагарин', 'Нагиев', 'Путин', 'Тесла', 'Эйнштейн', 'Соловьев', 'Киркоров', 'Ломоносов', 'Капица',
                      'Курчатов')
        result_people = random.sample(names_list, 5)

        for name in result_people:
            answer = input(f'Когда родился {name}? ')
            # correct += 1 if answer == dates.get(f'{name}') else incorrect += 1
            if answer == dates.get(f'{name}'):
                correct += 1
            elif answer == 'стоп':
                break
            else:
                incorrect += 1
            print('Правильный ответ', dates_words.get(f'{name}'))

        vol = correct / 5 * 100
        vol_2 = incorrect / 5 * 100
        print('У вас', correct, 'правильных ответов.')
        print('У вас', incorrect, 'неправильных ответов.')
        print('У Вас', vol, '% правильных ответов.')
        print('У Вас', vol_2, '% неправильных ответов.')
        again = input('Хотитет поиграть? ' 'Да / Нет ')
    else:
        print('Увидимся позже :)')


@decor
def change_directory():
    os.getcwd()
    print('Ваша текущая директория', os.getcwd())
    new_dir = input('Введите желаемую директорию ')
    os.chdir(f'{new_dir}')
    os.getcwd()
    print('Вы находитесь в', os.getcwd())
