from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class UserProfileManager(BaseUserManager):
    """Create a new User profile"""
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError('User must have an email address')
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,email,name,password):
        """Craete and save a new superuser with given deatils"""
        user=self.create_user(self,email,name,password)
        user.is_staff=True 
        user.is_superuser=True 
        user.save(using=self.db)
        return user 



class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database Model for users in the sysytem"""
    email=models.EmailField(max_length=255, unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        """Reterieve Full name of user"""
        return self.name
    def get_short_name(self):
        """Reterieve Short name of user"""
        return self.name
    
    def __str__(self):
        "Return string repreesntation of UserProfile class"
        return self.email
    



# Create your models here.
