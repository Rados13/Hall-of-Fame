from rest_framework import permissions
import jwt
from HallOfFame.settings import SECRET_KEY
from groups.api.permissions import get_id_from_token
from users.models import User


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        person = get_id_from_token(request)
        if person['user_id'] == obj.pk:
            return True
        return False


class IsLecture(permissions.IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        person = get_id_from_token(request)
        user = list(User.objects.filter(pk=person['user_id']))[0]
        if user.is_superuser or user.is_Lecture:
            return True
        return False
