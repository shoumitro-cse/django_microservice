from django.db import models

""" 
    Please, pay attention here.
    This document is a simple database design for a car company. 
    but I won't implement all kinds of logic in this database design. 
    I'll only implement some basic concepts of this design.   
"""
""""
    Cars Entity : Attributes of Cars are car_id, car_driver_id, car_customer_id, car_number, 
                  car_company car_type, car_description
    Car_Models Entity : Attributes of Car Models are car_model_id, car_model_number, car_model_year, 
                        car_model_name, car_model_type, car_model_description
    Car Owners Entity : Attributes of Car Owners are car owner_id, car owner_name, car owner_mobile, 
                        car owner_email, car owner_username, car owner_password, car owner_address
    Inventory Entity : Attributes of Inventory are inventory_id, inventory_items, inventory_number, 
                       inventory_type, inventory_description
    Customer Entity : Attributes of Customer are customer_id, customer_name, customer_mobile, 
                      customer_email, customer_username, customer_password, customer_address
    Booking Entity : Attributes of Booking are booking_id, booking_title, booking_type, booking_ticket, 
                     booking_date, booking_description
"""


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CarCompany(BaseModel):
    user_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    location = models.TextField()
    trade_licence = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Car Company'
        verbose_name_plural = 'Car Companies'


class Cars(BaseModel):
    car_number = models.PositiveIntegerField()
    car_company = models.ForeignKey(CarCompany, on_delete=models.CASCADE, related_name="cars")
    car_type = models.CharField(max_length=20)
    car_description = models.TextField()







