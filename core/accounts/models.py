from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser,PermissionMixin)


# Create your models here.
class User (AbstractBaseUser,PermissionMixin):
    """
    this is authentication model
    """
    username=models.CharField(max_length=250,unique=True)
    email=models.EmailField(max_length=255,unique=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    # is_verified=models.BooleanField(default=False)
    REQUIRED_FIELDS=[]

    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)


    def __str__(self):
        return self.username