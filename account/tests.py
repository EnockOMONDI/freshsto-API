from django.test import TestCase

# Create your tests here.


# class Supplier(models.Model):
#     supplier_id = models.AutoField(primary_key=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     company_name = models.TextField(max_length=127, blank=True, null=True)
#     company_logo =  CloudinaryField('image', blank=True, null=True)
#     phone_number = models.IntegerField(blank=True, null=True)
    
 
    
#     def __str__(self):
#         return self.user.first_name + " " + \
#                           self.user.last_name 
    
#     class Meta:
#         db_table = 'at_suppliers'

  
#     def create_supplier_profile(sender, **kwargs):
#         if kwargs['created']:
#             supplier = Supplier.objects.create(user=kwargs['instance'])

#     post_save.connect(create_supplier_profile, sender=User)


# class Vendor(models.Model):
#     vendor_id = models.AutoField(primary_key=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     company_name = models.TextField(max_length=127, blank=True, null=True)
#     phone_number = models.IntegerField(blank=True, null=True)
#     phone_number_2 = models.IntegerField(blank=True, null=True)
    
 
    
#     def __str__(self):
#         return self.user.first_name + " " + \
#                           self.user.last_name 
    
#     class Meta:
#         db_table = 'at_vendors'

  
#     def create_vendor_profile(sender, **kwargs):
#         if kwargs['created']:
#             vendor = Vendor.objects.create(user=kwargs['instance'])

#     post_save.connect(create_vendor_profile, sender=User)


from django.db import models
from django.contrib.auth.models import AbstractUser, Group , Permission
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
    is_supplier = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    
    # Add a related_name argument to the groups field
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions '
                    'granted to each of their groups.'),
        related_name='user_groups',
        related_query_name='user',
    )

    # Add a related_name argument to the user_permissions field
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='user_permissions',
        related_query_name='user',
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = CloudinaryField('image', blank=True, null=True)
    username = models.TextField(max_length=127, blank=True, null=True)
    apartment = models.TextField(max_length=127, blank=True, null=True)
    area_name = models.TextField(max_length=127, blank=True, null=True)
    house_no = models.TextField(max_length=127, blank=True, null=True)
    county = models.CharField(max_length=127, choices=COUNTY_CATEGORY_TYPES, blank=True,null=True,  default='Kenya')
    phone_number = models.IntegerField(blank=True, null=True)
    no_of_orders = models.PositiveIntegerField(default=0, blank=True)

    class Meta:
        abstract = True

    def has_discount(self):
        if self.no_of_orders > 0:
            return self.is_eligible

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name 


class Client(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='client_user',
    )


class Supplier(Profile):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='supplier_user',)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_logo = CloudinaryField('image', blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'account_supplier'


class Vendor(Profile):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='vendor_user',)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    phone_number_2 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'account_vendor'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        if instance.is_supplier:
            Supplier.objects.create(user=instance)
        elif instance.is_vendor:
            Vendor.objects.create(user=instance)
        else:
            Client.objects.create(user=instance)