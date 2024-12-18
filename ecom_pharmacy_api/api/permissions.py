from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to allow only admins to view the list of persons.
    Everyone can create a person (POST).
    """
    def has_permission(self, request, view):
        # Allow POST (creating a Person) for anyone
        if request.method == 'POST':
            return True
        # Allow viewing the list only for admin users
        return request.user and request.user.is_staff




class IsAdminOrStaffForWrite(BasePermission):
    """
    Custom permission to allow only admins or staff to create, update, and delete.
    Anyone can read (GET).
    """
    def has_permission(self, request, view):
        # Allow read-only (GET, HEAD, OPTIONS) for everyone
        if request.method in SAFE_METHODS:
            return True
        # Allow write permissions only to admins or staff
        return request.user and (request.user.is_staff or request.user.is_superuser)
