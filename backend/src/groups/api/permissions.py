from rest_framework import permissions
import jwt
from HallOfFame.settings import SECRET_KEY


def get_id_from_token(request):
    bearerToken = str(request['Authorization'])
    token = bearerToken[bearerToken.find(' ') + 1:]
    person = jwt.decode(token, SECRET_KEY)
    return person['user_id']


class IsOwnerOrReadOnly(permissions.BasePermission):

    # message =

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == 'DELETE':
            request = request.headers
        else:
            request = request.data['headers']
        id = get_id_from_token(request)
        lecture_list = list(map(lambda e: e.lecture_id, obj.lectures_list))
        if id in lecture_list:
            return True
        return False
