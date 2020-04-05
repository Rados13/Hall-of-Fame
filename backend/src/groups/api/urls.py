from django.urls import path
from .views import GroupAPIView,GroupRUDView

app_name = 'groups'
urlpatterns = [
    path('', GroupAPIView.as_view(), name='create'),
    path('<int:pk>/', GroupRUDView.as_view(), name='group-rud'),



]