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
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )


class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        token = get_authorization_header(request).decode().replace("Bearer", "").strip()
        payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms='HS256')
        user_id = payload.get("user_id", None)
        if user_id:
            auth_data = cache.get(user_id)
            if auth_data:
                print("auth_data: ", auth_data)
                return auth_data.get("auth")
            try:
                headers = {"Authorization": get_authorization_header(request).decode()}
                response = requests.get(f'http://localhost:8000/api/accounts/auth/user/{user_id}/', headers=headers)
                response.raise_for_status()
            except requests.exceptions.HTTPError as err:
                raise Exception(err)
            except Exception as err:
                raise Exception(err)
            cache.set(user_id, response.json())
            print("response.json(): ",  response.json())
            return response.json().get("auth")