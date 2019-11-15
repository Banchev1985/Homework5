import os
import platform
import sys
import shutil

# directory_path = input('Введите путь где вы хотите создать папку\название папки ')

# функция создания папки
from os.path import isdir


def new_directory():
    directiry_name = input('Напишите имя папки ')
    if not os.path.exists(directiry_name):
        os.mkdir(directiry_name)
    else:
        print('Такая папка существует, введите другое имя ')


# функция удаления файла/папки
def del_file():
    file_name = input('Введите имя файла ')
    os.remove(f'{file_name}')


# Удаление папки
def del_dir():
    dir_name = input('Введите имя папки ')
    os.rmdir(f'{dir_name}')
    print('Папка удалена')


# path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'{dir_name}')
# os.rmdir(path)


# копировать файл
def copy_file():
    old_file = input('Введите имя копируемого файла ')
    new_file = input('Введите новое имя файла ')
    shutil.copy(f'{old_file}', f'{new_file}')


def copy_directory():
    old_directory = input('Введите имя копируемой папки ')
    new_directory = input('Введите новое имя папки ')
    shutil.copytree(f'{old_directory}', f'{new_directory}')


# просмотр содержимого директории
def show_directory():
    arr = os.listdir('.')
    print(arr)


def system_info():
    print(platform.platform())


def dir_info():
    all_objects = os.listdir()
    dirs_only = []
    for item in all_objects:
        if os.path.isdir(item):
            dirs_only.append(item)
            print(dirs_only)


def file_info():
    all_objects = os.listdir()
    file_only = []
    for item in all_objects:
        if os.path.isfile(item):
            file_only.append(item)
            print(file_only)


# new_directory()
# del_dir()
# dir_info()

# Банковский баланс
def balanse():
    score = 0
    purchase = []

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню ')
        if choice == '1':
            score = int(input('На сколько пополнить счет? '))
            print(score)

        elif choice == '2':
            purchase_question_score = int(input('На какую суммы Вы хотите сделать покупку? '))
            if score < purchase_question_score:
                print('У Вас недостаточно средств на счете')
            else:
                purchase_question = input('Что вы хотите купить? ')
                purchase.append(purchase_question)
                score = score - purchase_question_score
                print(purchase)
                print(score)
        elif choice == '3':
            print('Вы купили', purchase)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')


def balance():
    score = 0
    purchase = []

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню ')
        if choice == '1':
            score = int(input('На сколько пополнить счет? '))
            print(score)

        elif choice == '2':
            purchase_question_score = int(input('На какую суммы Вы хотите сделать покупку? '))
            if score < purchase_question_score:
                print('У Вас недостаточно средств на счете')
            else:
                purchase_question = input('Что вы хотите купить? ')
                purchase.append(purchase_question)
                score = score - purchase_question_score
                print(purchase)
                print(score)
        elif choice == '3':
            print('Вы купили', purchase)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')


# Викторина
def victory():
    import random

    correct = 0
    incorrect = 0

    again = input('Хотитет поиграть? ' 'Да / Нет ')
    while again == 'Да':
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
            if answer == dates.get(f'{name}'):
                correct += 1
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


def change_directory():
    os.getcwd()
    print('Ваша текущая директория', os.getcwd())
    new_dir = input('Введите желаемую директорию ')
    os.chdir(f'{new_dir}')
    os.getcwd()
    print('Вы находитесь в', os.getcwd())



