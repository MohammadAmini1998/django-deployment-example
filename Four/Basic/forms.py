from Basic.models import UserPersonalInfo
from django.contrib.auth.models import User
from django import forms
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserPersonalInfo
        fields=('Profile_Link','Image_Profile')