from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from accounts import mixins
from accounts.authentication import IsAuthenticated as CustomIsAuthenticated


class IsAuthenticatedView(mixins.BaseUserViewMixin, generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        # from random import randint
        # a = True if randint(0, 1) else False
        # print('server: ', a)
        # return Response({"auth": a})
        return Response({"auth": bool(request.user and request.user.is_authenticated)})


class UserListCreateView(mixins.BaseUserViewMixin,
                         generics.ListCreateAPIView):
    """
    <div style='text-align: justify;'>
    This api is to be used to register like john, justin etc person account
    or to see all user lists. register api also open for Non-Authenticated user
    and Only Authenticated admin super will be able to see user lists.<br/>
    when an admin user try to send this request:
    <ul>
        <li> It performs register operation after sending a post request </li>
        <li> It gives a list of user after sending a get request.</li>
    </ul>
    </div>
    """
    permission_classes = [CustomIsAuthenticated, ]

    # def list(self, *args, **kwargs):
    #     message = "Non-Authenticated users can't access it."
    #     if self.request.user.is_authenticated:
    #         if self.request.user.is_superuser:
    #             return super().list(*args, **kwargs)
    #         message = "The user must be an admin to get all user data."
    #     return Response({"error": message}, status.HTTP_400_BAD_REQUEST)


class UserUpdateDeleteDestroyView(mixins.BaseUserViewMixin,
                                  generics.RetrieveUpdateDestroyAPIView):
    """
    <div style='text-align: justify;'>
    This API is used to get four HTTP methods functionality
    like get, put, patch, and delete for user crud operation.
    it is only for Authenticated users. <br/>Non-Authenticated users can't access it.
    when an admin user try to send this request:
    <ul>
        <li> It performs an update operation after sending a put request.</li>
        <li> It performs a partial update operation after sending a patch request.</li>
        <li> It performs a delete operation after sending a delete request.</li>
        <li> It gives the user details after sending a get request.</li>
    </ul>
    </div>
    """

    permission_classes = [IsAuthenticated, ]