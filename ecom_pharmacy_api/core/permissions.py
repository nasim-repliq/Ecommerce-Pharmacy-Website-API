from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrAdmin(BasePermission):
    """
    only the owner or admin/staff to access or modify.
    Everyone can create a person.
    """
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        # Allow all actions for admin/staff
        if request.user and (request.user.is_staff or request.user.is_superuser):
            return True
        # Restrict list view (GET without detail) for non-admin users
        if request.method == 'GET' and not view.kwargs.get('pk'):
            return False
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow admin/staff to perform any action
        if request.user and (request.user.is_staff or request.user.is_superuser):
            return True
        # Allow object-level access only if the user is the owner
        return obj == request.user





# from rest_framework.permissions import BasePermission, SAFE_METHODS

# class IsAdminOrReadOnly(BasePermission):
#     """
#     Custom permission to allow only admins to view the list of persons.
#     Everyone can create a person (POST).
#     """
#     def has_permission(self, request, view):
#         # Allow POST (creating a Person) for anyone
#         if request.method == 'POST':
#             return True
#         # Allow viewing the list only for admin users
#         return request.user and request.user.is_staff




# class IsAdminOrStaffForWrite(BasePermission):
#     """
#     Custom permission to allow only admins or staff to create, update, and delete.
#     Anyone can read (GET).
#     """
#     def has_permission(self, request, view):
#         # Allow read-only (GET, HEAD, OPTIONS) for everyone
#         if request.method in SAFE_METHODS:
#             return True
#         # Allow write permissions only to admins or staff
#         return request.user and (request.user.is_staff or request.user.is_superuser)
