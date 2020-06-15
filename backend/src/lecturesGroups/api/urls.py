from django.urls import path
from .views import *

app_name = 'lecturesGroups'
urlpatterns = [
    path('', LectureRetrieveAPIView.as_view(), name='lecture'),
    path('list/<int:pk>/', LecturesAPIView.as_view(), name='list'),

]
