from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permissions(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user == obj.creator