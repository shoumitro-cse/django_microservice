from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from company import mixins
from utils.authentication import IsAuthenticated as CustomIsAuthenticated
from company.producer import push_sms


class CarCompanyListCreateView(mixins.BaseCarCompanyViewMixin,
                               generics.ListCreateAPIView):
    """
    <div style='text-align: justify;'>
    This api is to be used to create car company record.
    or to see all CarCompany lists. register api also open for Non-Authenticated CarCompany
    and Only Authenticated admin super will be able to see CarCompany lists.<br/>
    when an admin CarCompany try to send this request:
    <ul>
        <li> It performs register operation after sending a post request </li>
        <li> It gives a list of CarCompany after sending a get request.</li>
    </ul>
    </div>
    """

    permission_classes = [CustomIsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        # push_sms("company_data", "Hello")
        return super().get(request, *args, **kwargs)


class CarCompanyUpdateDeleteDestroyView(mixins.BaseCarCompanyViewMixin,
                                        generics.RetrieveUpdateDestroyAPIView):
    """
    <div style='text-align: justify;'>
    This API is used to get four HTTP methods functionality
    like get, put, patch, and delete for Car Company crud operation.
    it is only for Authenticated Car Companies. <br/>Non-Authenticated Car Companies can't access it.
    when an admin CarCompany try to send this request:
    <ul>
        <li> It performs an update operation after sending a put request.</li>
        <li> It performs a partial update operation after sending a patch request.</li>
        <li> It performs a delete operation after sending a delete request.</li>
        <li> It gives the CarCompany details after sending a get request.</li>
    </ul>
    </div>
    """

    permission_classes = [IsAuthenticated, ]
