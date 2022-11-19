from django.core.cache import cache
from rest_framework.permissions import BasePermission
from rest_framework.authentication import get_authorization_header
import requests
from django.conf import settings
import jwt

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsAuthenticatedOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        token = get_authorization_header(request).decode().replace("Bearer", "").strip()
        payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms='HS256')
        user_id = payload.get("user_id", None)
        if user_id:
            key = f"{user_id}_is_authenticated_or_readonly"
            auth_data = cache.get(key)
            if auth_data:
                return auth_data.get("auth")
            try:
                headers = {"Authorization": get_authorization_header(request).decode()}
                response = requests.get(
                    f'http://localhost:8000/api/accounts/user/{user_id}/is-authenticated-or-readonly/', headers=headers)
                response.raise_for_status()
            except requests.exceptions.HTTPError as err:
                raise Exception(err)
            except Exception as err:
                raise Exception(err)
            cache.set(key, response.json())
            return response.json().get("auth")


class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        token = get_authorization_header(request).decode().replace("Bearer", "").strip()
        payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms='HS256')
        user_id = payload.get("user_id", None)
        if user_id:
            key = f"{user_id}_is_authenticated"
            auth_data = cache.get(key)
            if auth_data:
                return auth_data.get("auth")
            try:
                headers = {"Authorization": get_authorization_header(request).decode()}
                response = requests.get(f'http://localhost:8000/api/accounts/user/{user_id}/is-authenticated/', headers=headers)
                response.raise_for_status()
            except requests.exceptions.HTTPError as err:
                raise Exception(err)
            except Exception as err:
                raise Exception(err)
            cache.set(key, response.json())
            return response.json().get("auth")


class IsAdminUser(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        token = get_authorization_header(request).decode().replace("Bearer", "").strip()
        payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms='HS256')
        user_id = payload.get("user_id", None)
        if user_id:
            key = f"{user_id}_is_admin_user"
            auth_data = cache.get(key)
            if auth_data:
                return auth_data.get("auth")
            try:
                headers = {"Authorization": get_authorization_header(request).decode()}
                response = requests.get(f'http://localhost:8000/api/accounts/user/{user_id}/is-admin-user/', headers=headers)
                response.raise_for_status()
            except requests.exceptions.HTTPError as err:
                raise Exception(err)
            except Exception as err:
                raise Exception(err)
            cache.set(key, response.json())
            return response.json().get("auth")
