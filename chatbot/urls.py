# yomamabot/fb_yomamabot/urls.py
from django.urls import include, path
from .views import ChatBotView
urlpatterns = [
    path('6fd1410709aaf41f0f8682568db8447d53e348ce21842a7431/', ChatBotView.as_view()),
]


    # url(r'^7a080d34747afd2aa9ad88c429a3e775cffe526b485e813057/?$', YoMamaBotView.as_view()) 