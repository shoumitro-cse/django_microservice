from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from accounts import mixins


class IsAuthenticatedOrReadOnlyView(mixins.BaseUserViewMixin, generics.RetrieveAPIView):
    """
    The request is authenticated as a user, or is a read-only request.
    """
    permission_classes = [IsAuthenticated, ]
    # permission_classes = [IsAuthenticatedOrReadOnly, ]

    def get(self, request, *args, **kwargs):
        return Response({"auth": bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )})


class IsAuthenticatedView(mixins.BaseUserViewMixin, generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        return Response({"auth": bool(request.user and request.user.is_authenticated)})


class IsAdminUserView(mixins.BaseUserViewMixin, generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        return Response({"auth":  bool(request.user and request.user.is_staff)})