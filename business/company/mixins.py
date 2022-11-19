from rest_framework.permissions import AllowAny, IsAuthenticated
from company.models import CarCompany
from company.serializer import CarCompanySerializer


class BaseCarCompanyViewMixin:
    serializer_class = CarCompanySerializer
    permission_classes = [IsAuthenticated, ]
    queryset = CarCompany.objects.all().order_by("id")
