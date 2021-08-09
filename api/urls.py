
from django.contrib import admin
from django.urls import path, include

from api.views import DownloadFastTextModelAPIView, TrainCustomModel, GetPredictAPIView, \
    GetAvailiableFastTextModelsNameList

urlpatterns = [
    path('download', DownloadFastTextModelAPIView.as_view()),
    path('train', TrainCustomModel.as_view()),
    path('predict', GetPredictAPIView.as_view()),
    path('models_list', GetAvailiableFastTextModelsNameList.as_view()),
]
