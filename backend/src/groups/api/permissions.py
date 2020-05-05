from rest_framework import permissions
import jwt
from HallOfFame.settings import SECRET_KEY


def get_id_from_token(request):
    request = get_request_data(request)
    bearer_token = str(request['Authorization'])
    token = bearer_token[bearer_token.find(' ') + 1:]
    person = jwt.decode(token, SECRET_KEY)
    return person['user_id']


def get_request_data(request):
    if request.data == {}:
        return request.headers
    else:
        return request.data['headers']


class ReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False


class IsLecture(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        id = get_id_from_token(request)
        lecture_list = list(map(lambda e: e.lecture_id, obj.lectures_list))
        if id in lecture_list:
            return True
        return False


class IsStudent(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            id = get_id_from_token(request)
            lecture_list = list(map(lambda e: e.user_id, obj.enrolled_list))
            if id in lecture_list:
                return True
        return False

class PostMethod(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == "POST":
            return True
        return False
