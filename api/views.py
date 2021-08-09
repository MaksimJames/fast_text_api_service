from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema

from api.services import FastTextService
from api.serializers import DownloadFastTextModelSerializer, GetPredictSerializer, TrainCUstomModelSerializer, \
    AvailiableFastTextModelsSerializer
    

class DownloadFastTextModelAPIView(APIView, FastTextService):
    '''Скачиваем нужную нам модель fasttext'''
    serializer_class = DownloadFastTextModelSerializer
    
    @swagger_auto_schema(
        operation_description='Скачивание модели fasttext. Поиск и скачивание происходит исходя из того, какое значение ключа "lang" передано',
        request_body=DownloadFastTextModelSerializer,
    )
    def post(self, request):
        serializer = self.serializer_class(request.data)
        result = self.download_pretrained_fasttext_model(serializer.data['lang'])
        
        return Response(result)
    
    
class TrainCustomModel(APIView, FastTextService):
    serializer_class = TrainCUstomModelSerializer
    
    @swagger_auto_schema(
        operation_description='Тренируем нашу собственную модель. Для этого необходимо указать label и сам текст',
        request_body=TrainCUstomModelSerializer,
    )
    def post(self, request):
        serializer = self.serializer_class(request.data, many=True)
        result = self.train_custom_model(serializer.data)
        if not result:
            return Response('Something went wrong', status=500)
        
        return Response('Your model was train/retrain. \n'
                        'Now you can use this model')
        
        
class GetPredictAPIView(APIView, FastTextService):
    serializer_class = GetPredictSerializer
    
    @swagger_auto_schema(
        operation_description='Получаем предикт по нашим вводным данным. Если не указать model_name, \
            то по умолчанию будет использоваться кастомная модель.',
        request_body=GetPredictSerializer,
    )
    def post(self, request):
        serializer = self.serializer_class(request.data)
        result = self.get_predict(model_name=serializer.data['model_name'],
                                  text=serializer.data['text'])
        
        return Response(result)
    
    
class GetAvailiableFastTextModelsNameList(APIView, FastTextService):
    '''Вьюха для получения списка готовых к работе моделей'''
    serializer_class = AvailiableFastTextModelsSerializer
    
    @swagger_auto_schema(
        operation_description='Получаем список доступных к использованию моделей',
        responses={200: AvailiableFastTextModelsSerializer},
    )
    def get(self, request):
        result = self.get_availiable_models()
        serializer = self.serializer_class(result, many=True)
        
        return Response(serializer.data)
