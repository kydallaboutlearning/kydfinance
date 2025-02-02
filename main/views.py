from django.shortcuts import render,redirect
from django.utils.translation import get_language
from blog.models import BlogPost

# Create your views here.


def LandingPageView(request):
    posts = BlogPost.published.all()[:3]
    current_language = get_language()

    context = {
        'current_language': current_language,
        'posts':posts,
    }
    return render(request, 'main/home.html', context)


