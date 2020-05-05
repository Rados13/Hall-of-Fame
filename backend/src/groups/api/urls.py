from django.urls import path
from .views import GroupAPIView, GroupRUDView, StudentInGroupRUDView,MarkAllPostView

app_name = 'groups'
urlpatterns = [
    path('', GroupAPIView.as_view(), name='create'),
    path('<int:pk>/', GroupRUDView.as_view(), name='group-rud'),
    path('<int:pk>/markAll/', MarkAllPostView.as_view(), name='group-rud'),
    path('<int:pk>/student/', StudentInGroupRUDView.as_view(), name='studentInGroup-rud'),
    path('<int:pk>/students/', StudentInGroupRUDView.as_view(), name='studentInGroup-rud')

]
