'''
from django.db import models
from django.core import validators

class CustomUser(models.Model):
    mobile_no=models.IntegerField()#validators=[validators.MaxValueValidator(9999999999),validators.MinValueValidator(1000000000)])
    password=models.CharField(max_length=20)
    password_confirm=models.CharField(max_length=20)
    profile=models.CharField(max_length=20)

    def __str__(self):
        return str(self.mobile_no)


class Customer(models.Model):
    custom_user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    mobile_no = models.IntegerField()#validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(10)])
    password = models.CharField(max_length=20)


class Seller(models.Model):
    custom_user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    mobile_no = models.IntegerField()#validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(10)])
    password = models.CharField(max_length=20)
'''



from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    # email = models.EmailField(_('email address'), unique=True)
    email = models.EmailField(unique=True)
    mobile_no=models.BigIntegerField(unique=True)
    is_customer=models.BooleanField(default=False)
    is_seller=models.BooleanField(default=False)

    USERNAME_FIELD = 'mobile_no'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Customer(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Seller(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    company_name=models.CharField(max_length=50)
    gst_no=models.CharField(max_length=200)
    address=models.CharField(max_length=1000)
    bank_account=models.BigIntegerField()

    def __str__(self):
        return self.company_name




