# import part

from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser,PermissionsMixin)


# Create your models here.
# _________________________________________________________________________________________________________

class UserManager(BaseUserManager):
    """
    this is class to handle local users and super users
    """
    def create_user(self, email, password,**extra_fields):
        if not email:
            raise ValueError(_("the email must be set"))
        email= self.normalize_email(email)
        user= self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
     
    def create_superuser(self,email,password,**extra_fields):
        """
        this is class to handle local users
        """
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        if extra_fields.get ('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get ('is_superuser') is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))     
        return self.create_user(email,password,**extra_fields)


class User (AbstractBaseUser,PermissionsMixin):
    """
    this is authentication model
    """
    username=models.CharField(max_length=250,unique=True)
    email=models.EmailField(max_length=255,unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    # is_verified=models.BooleanField(default=False)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS=[]

    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)

    objects = UserManager()


    def __str__(self):
        return self.username