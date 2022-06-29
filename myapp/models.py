from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self,username, email, password, **extra_fields):
        if not username:
            raise ValueError(_('The username must be set'))
        if not email:
            raise ValueError(_('The Email must be set'))
        # username = self.normalize_username(username)
        # email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError(_('Superuser must have is_superuser=True.'))
        # return self.create_user(email, password, **extra_fields)
    
        if password is None:
            raise TypeError("Password should not be None")

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
    

# class User(AbstractBaseUser,PermissionsMixin):
#     username =models.CharField(max_length=250, unique=True, db_index=True)
#     email = models.EmailField(_('email address'), unique=True)
#     mobile =models.CharField(max_length=10, null=True, blank=True, db_index=True)
#     password = models.CharField(max_length=100)
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email', 'password']
#     object =CustomUserManager()

class User(AbstractBaseUser,PermissionsMixin):
    username =models.CharField(max_length=250, unique=True, db_index=True)
    email = models.EmailField(_('email address'), unique=True)
    mobile =models.CharField(max_length=10, null=True, blank=True, db_index=True)
    password = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']
    object =CustomUserManager()
    