from django.urls import path
from company import views

urlpatterns = [
    #  This URL is used for user registration and to see user lists
    path('car-company/', views.CarCompanyListCreateView.as_view(), name='car_company_create_list'),
    # This URL is used for a user to retrieve, partially or fully update and delete
    path('car-company/<int:pk>/', views.CarCompanyUpdateDeleteDestroyView.as_view(),
         name='car_company_retrieve_update_delete'),

    #  This URL is used for user registration and to see user lists
    path('car/', views.CarsListCreateView.as_view(), name='car_create_list'),
    # This URL is used for a user to retrieve, partially or fully update and delete
    path('car/<int:pk>/', views.CarUpdateDeleteDestroyView.as_view(),
         name='car_retrieve_update_delete'),
]