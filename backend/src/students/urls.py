from django.urls import path

from . import views

app_name = 'students'
urlpatterns = [
    # path('form', views.student_create_view, name='create'),
    # path('<int:id>/delete/', views.student_delete_view, name='delete'),
    # path('<int:id>', views.student_detail_view, name='view'),
    # path('', views.student_list , name='list'),
    path('', views.StudentListView.as_view(), name='list'),
    path('form/', views.StudentCreateView.as_view(), name='create'),
    path('<int:id>/', views.StudentDetailView.as_view(), name='view'),
    path('<int:id>/delete/', views.StudentDeleteView.as_view(), name='delete'),
    path('<int:id>/update/', views.StudentUpdateView.as_view(), name='update'),


]
