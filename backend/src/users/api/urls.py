from django.urls import path
from .views import UserRUDView, UserAPIView, UserInfo

app_name = 'users'
urlpatterns = [
    path('', UserAPIView.as_view(), name='user-create'),
    path('info/', UserInfo.as_view(), name='user-info'),
    path('<int:pk>/', UserRUDView.as_view(), name='user-rud'),
    path('<slug:type>/', UserAPIView.as_view(), name='users-type'),
]
