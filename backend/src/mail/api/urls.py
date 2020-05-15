from django.urls import path
from .views import *

app_name = 'mail'
urlpatterns = [
    path('', MailViewAPI.as_view(), name='send-mail'),
]