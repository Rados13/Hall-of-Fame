from django.urls import path
from .views import *

app_name = 'studentsGroups'
urlpatterns = [
    path('', StudentRetrieveAPIView.as_view(), name='student'),
    path('list/<int:pk>/', StudentsAPIView.as_view(), name='list'),
]
