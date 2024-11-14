from django.urls import path
from . import views

# アプリ名を登録
app_name = 'phonePushMessageApp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
