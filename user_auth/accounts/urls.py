from django.urls import path
from accounts import views

urlpatterns = [
    #  This URL is used for user registration and to see user lists
    path('user/', views.UserListCreateView.as_view(), name='create_list'),
    # This URL is used for a user to retrieve, partially or fully update and delete
    path('user/<int:pk>/', views.UserUpdateDeleteDestroyView.as_view(),
         name='user_retrieve_update_delete'),

    path('user/<int:pk>/is-authenticated/', views.IsAuthenticatedView.as_view(), name='is_authenticated_user'),
    path('user/<int:pk>/is-authenticated-or-readonly/', views.IsAuthenticatedOrReadOnlyView.as_view(),
         name='is_authenticated_or_readonly_user'),
]