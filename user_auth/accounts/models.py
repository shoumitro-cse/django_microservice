from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
import uuid


class User(AbstractUser):
    """ User class model used for authentication"""
    jwt_secret = models.UUIDField(default=uuid.uuid4)

    class Meta:
        db_table = "users_user"

    def jwt_get_secret_key(self):
        return self.jwt_secret

