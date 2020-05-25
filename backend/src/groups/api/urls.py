from django.urls import path
from .views import *

app_name = 'groups'
urlpatterns = [
    path('', GroupAPIView.as_view(), name='create'),
    path('stats/', StatsAPIView.as_view(), name='stats'),
    path('<int:pk>/', GroupRUDView.as_view(), name='group-rud'),
    path('<int:pk>/markAll/', MarkAllPostView.as_view(), name='mark-all'),
    path('<int:pk>/finalGrade/', FinalGradeAPIView.as_view(), name='mark-all'),
    path('<int:pk>/student/', StudentInGroupRUDView.as_view(), name='studentInGroup-rud'),
]
