from django.shortcuts import render,redirect
from django.utils.translation import get_language
from blog.models import BlogPost
from .models import  Newsletter
from .forms import NewsletterSub
from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from django.utils.translation import gettext_lazy as _



# Create your views here.

def LandingPageView(request):
    posts = BlogPost.published.all()[:3]
    current_language = get_language()

    if request.method == "POST":
        Newsletterform = NewsletterSub(request.POST)
        if Newsletterform.is_valid():
            user_email =  Newsletterform.cleaned_data["email"]
            new_sub = Newsletter.objects.create(email=user_email)
            
            # Render the email template with the translated content
            email_subject = _("Welcome to Our KYD-FINACE Newsletter")
            email_body = render_to_string("newsletter/newsletter_email.html", {"site_name": "KYD-FINANCE", "current_language": current_language})
            
            # Send email
            email = EmailMultiAlternatives(email_subject, "", settings.EMAIL_HOST_USER, [user_email])
            email.attach_alternative(email_body, "text/html")
            email.send()

            messages.success(request, _("Subscription successful! Check your email."))
            return redirect("main:landing-page")  # Redirect to avoid resubmission
        
    else:
        Newsletterform = NewsletterSub()

    context = {
        "current_language": current_language,
        "posts": posts,
        "Newsletterform": Newsletterform,
    }
    return render(request, "main/home.html", context)



