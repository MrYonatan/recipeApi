from rest_framework import permissions
from django.contrib.auth import get_user_model

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        return obj == request.user
    
