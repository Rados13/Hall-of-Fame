from django.urls import path
from .views import *

app_name = 'lectures'
urlpatterns = [
    path('', LectureRetrieveAPIView.as_view(), name='lecture'),
    path('list/', LecturesAPIView.as_view(), name='list'),

]
