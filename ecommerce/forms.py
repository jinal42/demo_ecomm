# from .models import UserProfile

from pyexpat import model
from .models import User,User1, UserReg
from  django import forms
# from django.contrib.auth.forms import UserCreationForm    

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password')

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['username','email','phone','gender']

class User1Form(forms.ModelForm):
    class Meta:
        model = User1
        fields = ['username','email','phone','gender','password']
        
# -------------------------------------


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserReg
        fields = ['phone','gender','user_type']

# class MyForm(forms.ModelForm):
    
#     class Meta:  
#         model= User1
#         fields = ['username']
