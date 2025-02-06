from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Comment
from django.utils.translation import gettext_lazy as _
import re


class NewsletterForm(forms.Form):
        email = forms.EmailField(max_length=200,widget=forms.EmailInput(attrs={
                                  "label":_("Email"),
                                  "required":True,
                                  "type":"email",
                                  "placeholder":_("Enter your Email")}))





class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "body"]
        labels = {
            "name": _("Your Name"),
            "email": _("Your Email"),
            "body": _("Comment"),
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": _("Enter your name"),
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": _("Enter your email"),
          
            }),
            "body": forms.Textarea(attrs={
                "placeholder": _("Write your comment here..."),
                "rows": 4,
            }),
        }

    # Custom Validation for Name
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) < 3:
            raise forms.ValidationError(_("Your name must be at least 3 characters long."))
        if not re.match(r"^[A-Za-z\s]+$", name):
            raise forms.ValidationError(_("Name should only contain letters and spaces."))
        return name

    # Custom Validation for Email
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            raise forms.ValidationError(_("Enter a valid email address."))
        return email

    # Custom Validation for Comment Body
    def clean_body(self):
        body = self.cleaned_data.get("body")
        if len(body) < 10:
            raise forms.ValidationError(_("Comment must be at least 10 characters long."))
        if len(body) > 500:
            raise forms.ValidationError(_("Comment cannot exceed 500 characters."))
        
        # Prevent spam-like content
        spam_keywords = ["http://", "https://", "buy now", "click here", "free money"]
        if any(spam in body.lower() for spam in spam_keywords):
            raise forms.ValidationError(_("Your comment contains spam-like content."))
        
        return body
