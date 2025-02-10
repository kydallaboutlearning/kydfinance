from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Comment
import re








class CommentForm(forms.Form): 
    body = forms.CharField(
        widget=forms.TextInput(attrs={
            "label":_("Enter your comment"),
            "placeholder": _("What's your thought on this..."),
            "type": "text",
        })
    )

    #  Custom Validation for Comment Body
    def clean_body(self):
        body = self.cleaned_data.get("body")

        if len(body) < 10:
            raise forms.ValidationError(_("Comment must be at least 10 characters long."))

        if len(body) > 500:
            raise forms.ValidationError(_("Comment cannot exceed 500 characters."))

        # Fix: Spam keywords should not use `_()`
        spam_keywords = ["http://", "https://", "buy now", "click here", "free money"]
        if any(spam in body.lower() for spam in spam_keywords):
            raise forms.ValidationError(_("Your comment contains spam-like content."))

        return body




class EmailPostForm(forms.Form):
    name = forms.CharField(
        max_length=25,
        widget=forms.TextInput(attrs={
            "placeholder": _("Enter your name."),
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "placeholder": _("Enter your email."),
            "type": "email",
        })
    )
    
    to = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "placeholder": _("Enter the recipient's email."),
            "type": "email",
        })
    )
    
    message = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": _("Write your comment here..."),
            "class": "comment__form form input",
        })
    )