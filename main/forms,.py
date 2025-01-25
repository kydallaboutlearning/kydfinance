# Importing requirements
from django import forms
from .models import Profile
from django.contrib.auth.models import User
from parler.forms import TranslatableModelForm


# creating RegistrationForm
class RegistrationForm(forms.Form):
     identifier = forms.CharField(max_length=200,
                                  label="Username ot Email",
                                  widget=forms.TextInput)
     password = forms.CharField(
          max_length=8, label='Password', widget= forms.PasswordInput
     )
     
     # A funstion to identify if  it's an emailor username
     def clean_identifier(self):
          context = self.cleaned_data
          identifier = context.get('identifier')

          # Check if the identifier is an email
          if "@" in identifier:  # If it contains "@" assume it's an email
               if not forms.EmailField().clean(identifier):
                    raise forms.ValidationError("Invalid email address.")
               if User.objects.filter(email=identifier).exists():
                    raise forms.ValidationError("A user with this email already exists.")
          else:  # Otherwise, treat it as a username
               if User.objects.filter(username=identifier).exists():
                    raise forms.ValidationError("A user with this username already exists.")

          return identifier

     
