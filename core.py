import datetime
import json
import os
import shutil


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    os.mkdir(name)


def get_list(path, folders_only=False):
    print('Текщая папка: ' + path)
    result = os.listdir(path)
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    else:
        result = [f for f in result]
    for f in result:
        print(f)


def delete_f(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_f(name, new_name):
    if os.path.isdir(name):
        shutil.copytree(name, new_name)
    else:
        shutil.copy(name, new_name)


def log(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def ch_dir(path, def_fld):
    os.chdir(path)
    with open(os.path.join(def_fld, 'active_dir.dat'), 'w') as f:
        json.dump(os.getcwd(), f)
    return os.getcwd()


if __name__ == '__main__':
    print(os.getcwd())
    print(type(os.getcwd()))
    # ch_dir(os.getcwd())
