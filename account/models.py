from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from cloudinary.models import CloudinaryField


COUNTY_CATEGORY_TYPES = (
('Westlands', 'Westlands'),
('Langata', 'Langata'),
('Kibra', 'Kibra'),
('Embakasi North', 'Embakasi North'),
('Embakasi South', 'Embakasi South'),
('Embakasi Central', 'Embakasi Central'),
('Embakasi West', 'Embakasi West'),
('Embakasi East', 'Embakasi East'),
('Makadara', 'Makadara'),
('Starehe', 'Starehe'),


)


class User(AbstractUser):
    is_client = models.BooleanField('is client', default=False)
    is_supplier = models.BooleanField('is supplier', default=False)
    is_vendor = models.BooleanField('is vendor', default=False)


class PrivateMessage(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=127)
    text = models.TextField()
    sent_date = models.DateField(auto_now_add=True, null=True)
    to_address = models.CharField(max_length=255)
    from_address = models.CharField(max_length=255)
    
    def __str__(self):
        return "From: " + self.from_address + " To: " + self.to_address + " Title: " + self.title
    
    class Meta:
        db_table = 'at_private_messages'


 

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    profile_pic =  CloudinaryField('image', blank=True, null=True)
    username = models.TextField(max_length=127, blank=True, null=True)
    apartment = models.TextField(max_length=127, blank=True, null=True)
    area_name = models.TextField(max_length=127, blank=True, null=True)
    house_no = models.TextField(max_length=127, blank=True, null=True)
    county = models.CharField(max_length=127, choices=COUNTY_CATEGORY_TYPES,  blank=True,null=True,  default='Kenya')
    phone_number = models.IntegerField(blank=True, null=True)
    no_of_orders=models.PositiveIntegerField(default=0)

    def has_discount(self):
    	if self.no_of_orders>0:
    		return self.is_eligible
    	
    def __str__(self):
        return self.user.first_name + " " + \
                           self.user.last_name 


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_logo = CloudinaryField('image', blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'account_supplier'

    def __str__(self):
        return self.user.first_name + " " + \
                           self.user.last_name

class Vendor(models.Model):
    Vendor_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    phone_number_2 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'account_vendor'

    def __str__(self):
        return self.user.first_name + " " + \
                           self.user.last_name