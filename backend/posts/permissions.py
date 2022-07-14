from rest_framework.permissions import BasePermission, SAFE_METHODS


class OnlyAuthor(BasePermission):
    message = "ONly author allowed !"

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
