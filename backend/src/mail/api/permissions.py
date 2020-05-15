from rest_framework import permissions
import jwt
from HallOfFame.settings import SECRET_KEY
from users.models import User

class ReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False

