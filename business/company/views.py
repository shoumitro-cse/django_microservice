from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from utils.authentication import IsAuthenticated as CustomIsAuthenticated
from company.models import CarCompany, Cars
from company.serializer import CarCompanySerializer, CarSerializer
from company.producer import push_sms


class CarCompanyListCreateView(generics.ListCreateAPIView):
    """
    <div style='text-align: justify;'>
    This api is to be used to create car company record. or to see all CarCompany lists for a user.
    <ul>
        <li> It performs register operation after sending a post request </li>
        <li> It gives a list of CarCompany after sending a get request.</li>
    </ul>
    </div>
    """

    permission_classes = [CustomIsAuthenticated, ]
    serializer_class = CarCompanySerializer

    def get_queryset(self):
        return CarCompany.objects.filter(user_id=self.request.user.pk).order_by("id")

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.pk)

    def get(self, request, *args, **kwargs):
        push_sms("company_data", {"data": "I'm from business app.", 'pk': self.request.user.pk})
        return super().get(request, *args, **kwargs)


class CarCompanyUpdateDeleteDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    <div style='text-align: justify;'>
    This API is used to get four HTTP methods functionality like get, put, patch, and delete for
    Car Company crud operation. it is only for Authenticated user that user secure by user_auth app.
    <br/>Non-Authenticated user can't access it.
    <ul>
        <li> It performs an update operation after sending a put request.</li>
        <li> It performs a partial update operation after sending a patch request.</li>
        <li> It performs a delete operation after sending a delete request.</li>
        <li> It gives the CarCompany details after sending a get request.</li>
    </ul>
    </div>
    """

    serializer_class = CarCompanySerializer
    permission_classes = [IsAuthenticated, ]
    queryset = CarCompany.objects.all().order_by("id")


class CarsListCreateView(generics.ListCreateAPIView):
    """
    <div style='text-align: justify;'>
    This api is to be used to create car record for a company. or to see all Car lists.
    <ul>
        <li> It performs register operation after sending a post request </li>
        <li> It gives a list of Car after sending a get request.</li>
    </ul>
    </div>
    """

    permission_classes = [CustomIsAuthenticated, ]
    serializer_class = CarSerializer

    def get_queryset(self):
        return Cars.objects.filter(car_company__user_id=self.request.user.pk).order_by("id")


class CarUpdateDeleteDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    <div style='text-align: justify;'>
    This API is used to get four HTTP methods functionality like get, put, patch, and delete
    for Car Company crud operation. it is only for Authenticated user that user secure by user_auth app.
    <br/>Non-Authenticated user can't access it.
    <ul>
        <li> It performs an update operation after sending a put request.</li>
        <li> It performs a partial update operation after sending a patch request.</li>
        <li> It performs a delete operation after sending a delete request.</li>
        <li> It gives the Car details after sending a get request.</li>
    </ul>
    </div>
    """

    serializer_class = CarSerializer
    permission_classes = [CustomIsAuthenticated, ]
