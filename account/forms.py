from django.db import models
from django import forms
from django.conf import settings
from django.forms import ModelForm
from django.contrib.auth.models import User
from account.models import PrivateMessage,Client, Vendor, Supplier
# from account.models import Profile,Post
import datetime
from django.forms import ModelForm, Textarea, TextInput, NumberInput, FileField, Select
# from django.forms.extras.widgets import Select, SelectDateWidget
from cloudinary.forms import CloudinaryFileField
from django.contrib.auth import get_user_model

user = get_user_model()

class PrivateMessageForm(forms.ModelForm):
    class Meta:
        model = PrivateMessage
        fields = ['from_address', 'title', 'text']
        labels = {
            'from_address': 'From',
        }

class UserForm(forms.ModelForm):
    class Meta:
        
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']

        widgets = {
            'first_name': TextInput(attrs={'class': u'form-control','placeholder': u'Enter First Name', 'required': True}),
            'last_name': TextInput(attrs={'class': u'form-control','placeholder': u'Enter Last Name', 'required': True}),
            'email': TextInput(attrs={'class': u'form-control','placeholder': u'Enter Email', 'required': True}),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if first_name is not None and first_name is not '':
            return first_name
        else:
            raise forms.ValidationError("Cannot be blank")

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if last_name is not None and last_name is not '':
            return last_name
        else:
            raise forms.ValidationError("Cannot be blank")

    def clean_email(self):
        email = self.cleaned_data['email']
        if email is not None and email is not '':
            return email
        else:
             raise forms.ValidationError("Cannot be blank")

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        
       
        try:
            email = cleaned_data.get("email")
            user = User.objects.get(email=email)
            if user != self.instance:
                raise forms.ValidationError("Email already exists")
        except User.DoesNotExist:
            pass

class ClientForm(forms.ModelForm):
    profile_pic = CloudinaryFileField(required=False,

        options = {
            'crop': 'thumb',
            'width': 200,
            'height': 200,
            'folder': 'profilepic'
       },
      
    ) 
    class Meta:
        model = Client
        fields = { 'profile_pic', 'county','apartment', 'username','house_no', 'area_name', 'phone_number'}
        labels = {
            'county': 'County :',
            'phone_number' : 'phone_number',

            'apartment' : 'apartment',
            'username' : 'username',
            'house_no ' : 'house_no',
            'area_name': 'area_name'
            
     }

        widgets = { 
            'apartment' : TextInput(attrs={'class': u'form-control','placeholder': u'eg Kivu Homes' }),
            'username': TextInput(attrs={'class': u'form-control','placeholder': u'eg champ'}),
            'house_no' : TextInput(attrs={'class': u'form-control','placeholder': u'Enter House No' }),
            'area_name' : TextInput(attrs={'class': u'form-control','placeholder': u'Enter Area Landmark' }),
            'county': Select(attrs={'class': u'form-control'}),
            'town': Select(attrs={'class': u'form-control'}),
            'phone_number': NumberInput(attrs={'class': u'form-control','placeholder': u'Enter your age here'}),
        }

