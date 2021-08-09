
import gzip
import shutil
import os

from django.conf import settings


def find_file_name():
    '''Утилита, которая ищет файлы с расширением .gz для передачи на распаковку'''
    path = settings.BASE_DIR
    needed_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.gz'):
                file.replace('.gz', '')
                needed_files.append(file)
        break
    
    return needed_files


def unpacking(file_name):
    '''Утилита, которая распаковывает файл из .gz, После удаляет .gz'''
    try:
        with gzip.open(f'{file_name}.gz', 'rb') as f_in:
            with open(file_name, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        return True
    except Exception as e:
        print(e)
        return False
    
    
def delete_unpacking_gz(file_name: str):
    try:
        os.remove(f'{file_name}.gz')
    except Exception as e:
        print(e)
            