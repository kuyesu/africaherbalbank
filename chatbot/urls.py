# # yomamabot/fb_yomamabot/urls.py
# from django.urls import include, path
# from .views import ChatBotView
# urlpatterns = [
#     path('6fd1410709aaf41f0f8682568db8447d53e348ce21842a7431/', ChatBotView.as_view()),
# ]


# urls.py

from django.urls import re_path
from django.contrib import admin

from .views import (
    FacebookWebhookView,
    )

app_name ='chatbot'

urlpatterns = [
    # replace <string_endpoint> with the one you created above
    re_path(r'^6c19a1c4e6dc3f500caa9dc0b2eff8131b2939d237f399b0386cf3c37da2/$', FacebookWebhookView.as_view(), name='webhook'),
]



# After replacing your pattern would look something like this:
# re_path(r'^d33300c2f7df8016b9f49f53179f9cae51/$', FacebookWebhookView.as_view(), name='webhook'),


    # url(r'^7a080d34747afd2aa9ad88c429a3e775cffe526b485e813057/?$', YoMamaBotView.as_view()) 