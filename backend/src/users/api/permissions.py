from rest_framework import permissions
import jwt
from HallOfFame.settings import SECRET_KEY


class IsOwnerOrReadOnly(permissions.BasePermission):



    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        bearerToken = str(request.headers['Authorization'])
        token = bearerToken[bearerToken.find(' ') + 1:]
        person = jwt.decode(token, SECRET_KEY)
        if person['user_id'] == obj.pk:
            return True
        return False
