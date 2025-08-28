from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def role_required(role_name):
    """
    A decorator that checks if a user has a specific role.
    """
    def check_role(user):
        # Checks if the user is authenticated and has the required role
        if user.is_authenticated and user.userprofile.role == role_name:
            return True
        # Otherwise, raise a permission denied exception or redirect
        raise PermissionDenied
    return user_passes_test(check_role)