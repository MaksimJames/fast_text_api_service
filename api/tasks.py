
import fasttext.util

from .celery import app
from .utils import unpacking, find_file_name, delete_unpacking_gz


@app.task
def download_fasttext_model_task(lang: str):
    '''
    Таск, который скачивает претренированную модель и распаковывает ее из архива.
    За прогрессом скачивания можно наблюдать в терминале в логах докера
    '''
    fasttext.util.download_model(lang, if_exists='ignore')
    file_name = find_file_name()
    unpacking_success = unpacking(file_name)
    delete_unpacking_gz(file_name)
    if unpacking:
        print('task was ended')
    else:
        print('error')