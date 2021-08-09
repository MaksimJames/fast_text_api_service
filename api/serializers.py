
from rest_framework.serializers import Serializer, CharField


class DownloadFastTextModelSerializer(Serializer):
    '''Сериализатор для скачивания модели по языку'''
    lang = CharField(min_length=2, max_length=2, required=True)
    
    
class GetPredictSerializer(Serializer):
    '''Сериализатор для получения предикта по нашим вводным данным'''
    model_name = CharField(help_text='По умолчанию будет использоваться наша кастомная модель')
    text = CharField(min_length=1, required=True)
    
    
class TrainCUstomModelSerializer(Serializer):
    '''Сериализатор для обучения/переобучения нашей кастомной модели'''
    label = CharField(required=True)
    text = CharField(required=True)
    
    
class AvailiableFastTextModelsSerializer(Serializer):
    '''Сериализатор для получения списка готовых к использованию моделей'''
    name = CharField()