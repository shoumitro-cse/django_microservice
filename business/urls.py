from django.urls import path
from accounts import views

urlpatterns = [
    #  This URL is used for user registration and to see user lists
    path('user/', views.CarCompanyListCreateView.as_view(), name='create_list'),
    # This URL is used for a user to retrieve, partially or fully update and delete
    path('user/<int:pk>/', views.CarCompanyUpdateDeleteDestroyView.as_view(),
         name='user_retrieve_update_delete'),

    path('auth/user/<int:pk>/', views.IsAuthenticatedView.as_view(), name='is_authenticated_user'),
]