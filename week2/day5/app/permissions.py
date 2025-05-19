from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        role = request.headers.get("Authorization", "")
        return role == "admin"