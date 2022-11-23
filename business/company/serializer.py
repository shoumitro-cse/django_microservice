from company.models import CarCompany, Cars
from rest_framework import serializers


class CarCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = CarCompany
        fields = ["name", "location", "trade_licence"]


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cars
        fields = '__all__'
