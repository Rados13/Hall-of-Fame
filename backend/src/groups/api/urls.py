from django.urls import path
from .views import GroupAPIView, GroupRUDView, StudentInGroupRUDView

app_name = 'groups'
urlpatterns = [
    path('', GroupAPIView.as_view(), name='create'),
    path('<int:pk>/', GroupRUDView.as_view(), name='group-rud'),
    path('<int:pk>/student/', StudentInGroupRUDView.as_view(), name='studentInGroup-rud')

]
