
import os

import fasttext.util
from django.conf import settings

from api.tasks import download_fasttext_model_task


class FastTextService:
    '''Класс/сервис для работы с моделями fasttext'''
    
    def get_availiable_models(self):
        path = settings.BASE_DIR
        availiable_models_list = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.bin'):
                    print(file)
                    availiable_models_list.append({'name': file})
            break
                
        return availiable_models_list
    
    def download_pretrained_fasttext_model(self, lang: str):
        '''Скачиваем нужную нам модель с сайта fasttext'''
        download_fasttext_model_task.delay(lang)
        response_data = 'Скачивание модели началось. За прогрессом скачивания можете следить в терминале, если запускали контейнер без "-d" :). \
                        После загрузки модель будет доступна по эндпоинту /predict'
        
        return response_data
    
    def train_custom_model(self, data):
        '''
            Тренируем нашу собственную модель. При добавлении данных, данные добавляются в файл обучения,
            модель переобучается и обновляется. В случае успеха можно пользоваться обученной моделью.
            В случае ошибки Вы получите соответствующее сообщение.
        '''
        try:
            for i in data:
                label = i['label']
                text = i['text']
                with open('test_data.txt', 'a+') as f: # <--- Добавляем новые данные в существующий .txt 
                    f.seek(0, 2)
                    f.write(f'__label__{label} {text} \n')
            model = fasttext.train_supervised(input="test_data.txt", epoch=100)
            model.save_model("test_model.bin")
            
            return {'it seems like everything ok :)'}
        except Exception as e:
            print(e)
            return False
        
    def get_predict(self, model_name: str=None, text: str=None):
        '''Получаем предикт по нашим вводным данным'''
        model = fasttext.load_model('test_model.bin')
        if model_name:
            model = fasttext.load_model(f'{model_name}')
        predict = model.predict(f'{text}')
        category = predict[0][0].split('__')[2]
        accurancy = round(predict[1][0] * 100, 2)
        response_data = f'Your predict is: {category} with {accurancy}%. I think...'
        
        return response_data
