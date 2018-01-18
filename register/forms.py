from django import forms
from .models import Contracts, Organization, Company


class LoginForm(forms.Form):
    username = forms.EmailField(label="Username",help_text="Your Username")
    password = forms.PasswordInput()


class RegisterForm(forms.Form):
    name = forms.CharField(label="Full name", help_text="Enter your full name")
    email = forms.EmailField(label="Email", help_text="Enter your Email-id")
    password = forms.PasswordInput()
    # class Meta:
    #   model = Organization
    #   fields = ['name', 'email', 'password']


class RegisterContracts(forms.ModelForm):
    class Meta:
        model = Contracts
        fields = ['name', 'description', 'location']

    # name = forms.CharField(label="Full name", help_text="Enter your full name")
    # desc = forms.EmailField(label="Email", help_text="Enter your Email-id")
    # location = forms.PasswordInput()