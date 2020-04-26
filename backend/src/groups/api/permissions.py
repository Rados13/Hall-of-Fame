from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    # message =

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Some condition
        return False


