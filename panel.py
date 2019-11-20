import functions

while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет ')
    print('11. смена рабочей директории ')
    print('12. выход ')
    panel = input('Выберите пункт меню ')
    if panel == '1':
        functions.new_directory()
    elif panel == '2':
        print('1. Папка')
        print('2. Файл')
        delete = input('Что Вы хотите удалить? ')
        if delete == 1:
            functions.del_dir()
        elif delete == 2:
            functions.del_file()
    elif panel == '3':
        print('1. Папка')
        print('2. Файл')
        copy = input('Что Вы хотите скопировать? ')
        if copy == 1:
            functions.copy_directory()
        elif copy == 2:
            functions.copy_file()
    elif panel == '4':
        functions.show_directory()
    elif panel == '5':
        functions.dir_info()
    elif panel == '6':
        functions.file_info()
    elif panel == '7':
        functions.system_info()
    elif panel == '8':
        print('Эту прогрпмму написал Банчев Александр')
    elif panel == '9':
        functions.victory()
    elif panel == '10':
        functions.balance()
    elif panel == '11':
        functions.change_directory()
    elif panel == '12':
        break
    else:
        print('Неверный пункт меню')
