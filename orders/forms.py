from django.db import models
from django import forms
from django.conf import settings
from django.forms import ModelForm
from django.contrib.auth.models import User
from  orders.models import *
import datetime
from django.forms import ModelForm, Textarea, TextInput, NumberInput, FileField, CheckboxInput, Select 




class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = { 'first_name', 'last_name', 'street_name', 'email', 'location', 'area', 'phone', 'house_number'}



