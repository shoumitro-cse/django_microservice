from django.core.cache import cache
from rest_framework.permissions import BasePermission
from rest_framework.authentication import get_authorization_header
import requests
from django.conf import settings
import jwt

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class AuthPermission(BasePermission):
    def get_user(self, request):
        bearer_token = get_authorization_header(request)
        if bearer_token:
            token = bearer_token.decode().replace("Bearer", "").strip()
            payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms='HS256')
            return payload.get("user_id", False)
        return False


class IsAuthenticatedOrReadOnly(AuthPermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        user_id = self.get_user(request)
        if user_id:
            key = f"{user_id}_is_authenticated_or_readonly"
            auth_data = cache.get(key)
            if auth_data:
                return auth_data.get("auth")
            try:
                headers = {"Authorization": get_authorization_header(request).decode()}
                response = requests.get(
                    f'http://localhost:8000/api/accounts/user/is-authenticated-or-readonly/', headers=headers)
                response.raise_for_status()
            except requests.exceptions.HTTPError as err:
                raise Exception(err)
            except Exception as err:
                raise Exception(err)
            cache.set(key, response.json())
            return response.json().get("auth")


class IsAuthenticated(AuthPermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        user_id = self.get_user(request)
        if user_id:
            key = f"{user_id}_is_authenticated"
            auth_data = cache.get(key)
            if auth_data:
                return auth_data.get("auth")
            try:
                headers = {"Authorization": get_authorization_header(request).decode()}
                response = requests.get(f'http://localhost:8000/api/accounts/user/is-authenticated/', headers=headers)
                response.raise_for_status()
            except requests.exceptions.HTTPError as err:
                raise Exception(err)
            except Exception as err:
                raise Exception(err)
            cache.set(key, response.json())
            return response.json().get("auth")
        return False


class IsAdminUser(AuthPermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        user_id = self.get_user(request)
        if user_id:
            key = f"{user_id}_is_admin_user"
            auth_data = cache.get(key)
            if auth_data:
                return auth_data.get("auth")
            try:
                headers = {"Authorization": get_authorization_header(request).decode()}
                response = requests.get(f'http://localhost:8000/api/accounts/user/is-admin-user/', headers=headers)
                response.raise_for_status()
            except requests.exceptions.HTTPError as err:
                raise Exception(err)
            except Exception as err:
                raise Exception(err)
            cache.set(key, response.json())
            return response.json().get("auth")
