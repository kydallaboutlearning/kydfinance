from django import forms
from .models import Newsletter
from django.utils.translation import gettext_lazy as _


class NewsletterForm(forms.Form):
        email = forms.EmailField()