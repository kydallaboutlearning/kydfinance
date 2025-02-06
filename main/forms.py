from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Newsletter
import logging
from django import forms



# Configure logger
logger = logging.getLogger(__name__)


class NewsletterSub(forms.Form):
        
        email = forms.EmailField(max_length=200,widget=forms.EmailInput(attrs={
                                  "label":_("Email"),
                                  "required":True,
                                  "type":"email",
                                  "placeholder":_("Enter your Email")}))

        def clean_email(self):
                email = self.cleaned_data.get('email')

                if Newsletter.objects.filter(email=email).exists():
                        logger.info(f"Duplicate email attempt: {email}")  # Log before raising error
                        raise forms.ValidationError(_('Email already exists'))

                return email