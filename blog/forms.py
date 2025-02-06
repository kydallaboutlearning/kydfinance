from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Comment
import re








class CommentForm(forms.Form):
        body = forms.CharField( widget =forms.Textarea(attrs={
                "placeholder": _("Write your comment here..."),
                "rows": 4,
                "type":"text",

            }))

 

    
        # Custom Validation for Comment Body
        def clean_body(self):
                body = self.cleaned_data.get("body")
                if len(body) < 10:
                        raise forms.ValidationError(_("Comment must be at least 10 characters long."))
                if len(body) > 500:
                        raise forms.ValidationError(_("Comment cannot exceed 500 characters."))
        
                # Prevent spam-like content
                spam_keywords = ["http://", "https://",_( "buy now"), _("click here"), _("free money")]
                if any(spam in body.lower() for spam in spam_keywords):
                        raise forms.ValidationError(_("Your comment contains spam-like content."))
        
                return body
