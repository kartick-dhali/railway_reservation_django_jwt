from rest_framework.permissions import BasePermission

class IsAdminOrUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role in ['ADMIN', 'USER']
        return False

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role=='ADMIN'
    
class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role=='USER'