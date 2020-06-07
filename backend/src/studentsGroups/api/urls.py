from django.urls import path
from .views import *

app_name = 'student'
urlpatterns = [
    path('', StudentRetrieveAPIView.as_view(), name='student'),
    path('list/', StudentsAPIView.as_view(), name='list'),
]
