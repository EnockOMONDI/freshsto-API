from django.contrib import admin
from account.models import PrivateMessage
from account.models import Client, Vendor, Supplier

# from account.models import UserProfile

admin.site.register(PrivateMessage)
admin.site.register(Client)
admin.site.register(Vendor)
admin.site.register(Supplier)
