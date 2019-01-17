from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsUserOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, user):
        if request.method in SAFE_METHODS:
            return True
        return request.user is user


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner is request.user


class IsSuperuserOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_superuser


