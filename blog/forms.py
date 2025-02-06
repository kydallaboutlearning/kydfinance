from django import forms
from django.utils.translation import gettext_lazy as _


class NewsletterForm(forms.Form):
        email = forms.EmailField(max_length=200,widget=forms.EmailInput(attrs={
                                  "label":_("Email"),
                                  "required":True,
                                  "type":"email",
                                  "placeholder":_("Enter your Email")}))