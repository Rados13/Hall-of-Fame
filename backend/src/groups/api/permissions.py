from rest_framework import permissions
import jwt
from HallOfFame.settings import SECRET_KEY
from users.models import User


def get_user_from_request(request):
    user_id = get_id_from_token(request)
    return list(User.objects.filter(pk=user_id))[0]


def get_id_from_token(request):
    request = get_request_data(request)
    bearer_token = str(request['Authorization'])
    token = bearer_token[bearer_token.find(' ') + 1:]
    person = jwt.decode(token, SECRET_KEY)
    return person['user_id']


def get_request_data(request):
    if request.data == {} or 'headers' not in request.data:
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
        lecture_list = [elem.lecture.pk for elem in obj.lectures_list]
        if id in lecture_list:
            return True
        return False


class IsLectureOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        id = get_id_from_token(request)
        lecture_list = [elem.lecture.pk for elem in obj.lectures_list]
        if id in lecture_list:
            return True
        return False


class IsStudent(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            id = get_id_from_token(request)
            students_list = [elem.student.pk for elem in obj.enrolled_list]
            if id in students_list:
                return True
        return False


class PostMethod(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == "POST":
            return True
        return False
