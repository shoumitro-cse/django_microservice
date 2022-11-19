from company.models import CarCompany
from rest_framework import serializers


class CarCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = CarCompany
        fields = '__all__'
