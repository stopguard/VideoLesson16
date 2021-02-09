"""
1. В консольный файловый менеджер добавить проверку ввода пользователя для всех функции с параметрами
   (на уроке разбирали на примере одной функции).

2. Добавить возможность изменения текущей рабочей директории.

3. Добавить возможность развлечения в процессе работы с менеджером.
   Для этого добавить в менеджер запуск одной из игр: “угадай число” или “угадай число (наоборот)”.
"""
import json
import os
import sys

from core import create_file, create_folder, get_list, delete_f, copy_f, ch_dir, log

act = ''
def_fld = os.getcwd()

try:
    with open('active_dir.dat', 'r') as f:
        active_dir = json.load(f)
except:
    active_dir = def_fld


def helper():
    global act
    print('list - список файлов и папок')
    print('list folders - список папок')
    print('chdir <путь> - изменение активной папки')
    print('game - игра')
    print('default - смена активной папки на папку программы')
    print('\nВсе пути для команд ниже указываются относительно активной папки!')
    print('create_file <имя файла> - создать файл')
    print('create_folder <имя папки> - создать папку')
    print('delete <имя файла/папки> - удалить файл/папку')
    print('copy <имя файла/папки> - скопировать файл/папку')
    act = 'help'


log(sys.argv)

if len(sys.argv) > 1:
    command = sys.argv[1]
    act = command
else:
    command = ''

try:
    if command == 'list':
        get_list(active_dir, True) if len(sys.argv) > 2 and sys.argv[2] == 'folders' else get_list(active_dir)

    elif command == 'create_file':
        name = sys.argv[2]
        try:
            text = sys.argv[3]
        except IndexError:
            create_file(os.path.join(active_dir, name))
        else:
            create_file(os.path.join(active_dir, name), text)

    elif command == 'create_folder':
        name = sys.argv[2]
        create_folder(os.path.join(active_dir, name))

    elif command == 'delete':
        name = sys.argv[2]
        delete_f(os.path.join(active_dir, name))

    elif command == 'chdir':
        name = sys.argv[2]
        print('Рабочая папки изменена. Содержимое:')
        get_list(ch_dir(os.path.join(active_dir, name), def_fld))

    elif command == 'copy':
        name = sys.argv[2]
        new_name = sys.argv[3]
        copy_f(os.path.join(active_dir, name), os.path.join(active_dir, new_name))

    elif command == 'game':
        import game

    elif command == 'default':
        delete_f('active_dir.dat')
        print('Рабочая папкa изменена. Содержимое:')
        get_list(def_fld)

    else:
        helper()
except IndexError:
    log('Не указано название файла/папки')
    print('\nНе указано название файла/папки\n')
    helper()
except FileExistsError:
    print(f'\nПапка с таким именем уже существует\n')
    log(f'Папка с таким именем уже существует')
except FileNotFoundError:
    log('Такого файла/папки не существует')
    print('\nТакого файла/папки не существует\n')
    helper()
except OSError:
    log('Синтаксическая ошибка в имени файла/папки')
    print('\nСинтаксическая ошибка в имени файла/папки\n')
    helper()
else:
    print('Выполнено успешно: ', act)
    log('Выполнено успешно: ' + act)
