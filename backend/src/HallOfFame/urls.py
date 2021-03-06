"""HallOfFame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('api/users/', include('users.api.urls', namespace='api-users', )),
    path('api/groups/', include('groups.api.urls', namespace='api-groups', )),
    path('api/lecturesGroups/', include('lecturesGroups.api.urls', namespace='api-lecturesGroups', )),
    path('api/studentsGroups/', include('studentsGroups.api.urls', namespace='api-studentsGroups', )),
    path('api/mail/', include('mail.api.urls',namespace='mail')),
    path('api/token', TokenObtainPairView.as_view(), name='api-login'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='api-login'),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
