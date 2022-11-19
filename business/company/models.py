from django.db import models


class CarCompany(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField()

    class Meta:
        verbose_name = 'Car Company'
        verbose_name_plural = 'Car Companies'

