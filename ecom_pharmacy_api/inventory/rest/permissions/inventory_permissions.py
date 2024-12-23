from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminUser(BasePermission):
    """Allows full access for admin users."""
    def has_permission(self, request, view):
        return request.user.is_staff or request.user.is_superuser


class IsOwner(BasePermission):
    """Allows owners to manage their own inventory."""
    def has_object_permission(self, request, view, obj):
        # Check if the user is an owner of the organization
        return obj.shop.personorganization_set.filter(
            user=request.user, role__in=["owner"]
        ).exists()


class IsAuthenticatedReadOnly(BasePermission):
    """Allows authenticated users to view inventory."""
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS and request.user.is_authenticated
