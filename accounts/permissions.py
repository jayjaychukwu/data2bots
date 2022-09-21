from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    # Does not allow users not logged in
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    # Does not allow others except the owner access to its fields
    def has_object_permission(self, request, view, obj):
        return obj.email == request.user.email
