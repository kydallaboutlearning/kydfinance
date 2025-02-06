from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Newsletter


class NewsletterSub(forms.Form):
        email = forms.EmailField()
        # A funstion to identify if  it's an emailor username
        def clean_email(self):
                context = self.cleaned_data
                email = context.get('email')

                if Newsletter.objects.filter(email=email).exists():
                        raise forms.ValidationError(_('Email already exists'))
                return email