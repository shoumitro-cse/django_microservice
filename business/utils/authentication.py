from django.core.cache import cache
from rest_framework.permissions import BasePermission
from rest_framework.authentication import get_authorization_header
import requests
from django.conf import settings
import jwt

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class UserAuthPermission(BasePermission):

    def get_auth_permission(self, request, suffix_key, path_url):
        user_id = self.get_user(request)
        if user_id:
            key = f"{user_id}_{suffix_key}"
            auth_data = cache.get(key)
            if auth_data:
                return auth_data.get("auth")
            try:
                headers = {"Authorization": get_authorization_header(request).decode()}
                response = requests.get(f'{settings.AUTH_USER_SERVICE_URL}{path_url}', headers=headers)
                response.raise_for_status()
            except requests.exceptions.HTTPError as err:
                raise Exception(err)
            except Exception as err:
                raise Exception(err)
            cache.set(key, response.json())
            return response.json().get("auth")
        return False

    def get_user(self, request):
        bearer_token = get_authorization_header(request)
        # token = request.user.token
        if bearer_token:
            token = bearer_token.decode().replace("Bearer", "").strip()
            payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms='HS256')
            return payload.get("user_id", False)
        return False


class IsAuthenticatedOrReadOnly(UserAuthPermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return self.get_auth_permission(request, suffix_key="is_authenticated_or_readonly",
                                        path_url="/api/accounts/user/is-authenticated-or-readonly/")


class IsAuthenticated(UserAuthPermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return self.get_auth_permission(request, suffix_key="is_authenticated",
                                        path_url="/api/accounts/user/is-authenticated/")


class IsAdminUser(UserAuthPermission):
    """
    Allows access only to authenticated users.
    """
    def has_permission(self, request, view):
        return self.get_auth_permission(request, suffix_key="is_admin_user",
                                        path_url="/api/accounts/user/is-admin-user/")