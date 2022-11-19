import requests
from django.core.cache import cache
from django.conf import settings
# from accounts.authentication import get_permission_data
from rest_framework.permissions import BasePermission
from rest_framework.authentication import get_authorization_header
import requests
from django.conf import settings
import jwt
import json


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
                response = requests.get(f'http://localhost:8000/api/accounts/user/{user_id}/is-authenticated/', headers=headers)
                response.raise_for_status()
            except requests.exceptions.HTTPError as err:
                raise Exception(err)
            except Exception as err:
                raise Exception(err)
            cache.set(user_id, response.json())
            print("response.json(): ",  response.json())
            return response.json().get("auth")


# def get_permission_data(self, request, path=None):
#     key = '{user_id}_{path}'.format(user_id=request.user.id, path=path)
#     data = cache.get(key)
#     if data:
#         return data
#     try:
#         headers = {"Authorization": get_authorization_header(request)}
#         r = requests.get(settings.AUTH_SERVER_PREFIX + path, headers=headers)
#         r.raise_for_status()
#     except requests.exceptions.HTTPError as err:
#         raise Exception(err)
#     except Exception as err:
#         raise Exception(err)
#     cache.set(key, r.json())
#     return r.json()
#
#
# class EditPermission(BasePermission):
#     def has_permission(self, request, view):
#         user_id = view.kwargs.get('user_id')
#         permission_data = get_permission_data(request, f'/user/permission/edit/{user_id}')
#         return "edit" in permission_data.get("permission")


# class IsAuthenticated(BasePermission):
#     """
#     Allows access only to authenticated users.
#     """
#
#     def has_permission(self, request, view):
#         token = get_authorization_header(request).decode().replace("Bearer", "").strip()
#         # print(token)
#         # print()
#         payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms='HS256')
#         print(payload)
#
#         token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2OTQ4Mzc5OCwiaWF0IjoxNjY4ODc4OTk4LCJqdGkiOiIyOGYzYzUyZTA4Yzg0YmEzYjE5NzQ3NTczMzJmMzE1YiIsInVzZXJfaWQiOjF9.Br9eT5rX0GeLU-ow1Cx0G7Eibz21fhVqTG4bJ_-dCDE"
#         payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms='HS256')
#         print(payload)
#         return True
#         # return bool(request.user and request.user.is_authenticated)




# from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication, \
#     JWTAuthentication as BaseJWTAuthentication
# from django.utils.translation import gettext_lazy as _
# from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken
# from rest_framework_simplejwt.settings import api_settings
#
#
# class JWTAuthentication(BaseJWTAuthentication):
#
#     def get_user(self, validated_token):
#         """
#         Attempts to find and return a user using the given validated token.
#         """
#         try:
#             user_id = validated_token[api_settings.USER_ID_CLAIM]
#         except KeyError:
#             raise InvalidToken(_("Token contained no recognizable user identification"))
#
#         try:
#             user = self.user_model.objects.get(**{api_settings.USER_ID_FIELD: user_id})
#         except self.user_model.DoesNotExist:
#             raise AuthenticationFailed(_("User not found"), code="user_not_found")
#
#         if not user.is_active:
#             raise AuthenticationFailed(_("User is inactive"), code="user_inactive")
#
#         return user
