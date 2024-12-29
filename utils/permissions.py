from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsVendorOrAdmin(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and (request.user.is_superuser or request.user.role == "VENDOR")
        )

    def has_object_permission(self, request, view, obj):
        # Check if the object's owner is the requesting user
        return request.user.is_superuser or obj.user == request.user


class IsVendorOrAdminOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and (request.user.is_superuser or request.user.role == "VENDOR")
        )

    def has_object_permission(self, request, view, obj):
        # Check if the object's owner is the requesting user
        return request.user.is_superuser or obj.user == request.user