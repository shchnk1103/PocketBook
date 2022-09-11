from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the pocket_books.
        # If request.user is superuser, this user has all permissions.
        if request.user.is_staff:
            return True

        # If request.user isn't superuser, this user can only check own permission.
        return obj == request.user
