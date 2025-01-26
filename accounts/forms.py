# Importing requirements
from django import forms
from .models import Profile
from django.contrib.auth.models import User
from parler.forms import TranslatableModelForm
from django.core.validators import MinLengthValidator, MaxLengthValidator
#importing gettext_lazy for translation
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import PasswordChangeForm as BasePasswordChangeForm

# creating RegistrationForm
class RegistrationForm(forms.Form):
     email = forms.EmailField(max_length=200,widget=forms.EmailInput(attrs={
                                  "label":_("Email"),
                                  "required":True,
                                  "type":"email",
                                  "placeholder":_("Enter your Email")}))
  
     username = forms.CharField(max_length=200,
                                 widget=forms.TextInput(attrs={
                                  "label":_("Username"),
                                  "required":True,
                                  "type":"text",
                                  "placeholder":_("Enter your Username")}))
     
     password = forms.CharField(label=_('Password'), widget= forms.PasswordInput(attrs={
                                  "label":_("Username"),
                                  "required":True,
                                  "type":"password",
                                  "placeholder":_("Enter your Password")}),
          validators=[MinLengthValidator(4,_('The password must be a minimum of 4 characters '))]
     )
     
     # A funstion to identify if  it's an emailor username
     def clean_email(self):
          context = self.cleaned_data
          email = context.get('email')

          if User.objects.filter(email=email).exists():
               raise forms.ValidationError(_('Email already exists'))
          return email
     
     # a function to clean the form

     def clean(self):    
        cleaned_data = super().clean()
        email  = cleaned_data.get("email")
        username  = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if not email or not password or not username:
            raise forms.ValidationError(_("Both fields are required."))

        return cleaned_data


