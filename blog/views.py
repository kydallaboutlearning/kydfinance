from django.shortcuts import render
from .models import BlogPost

# Create your views here.

def post_list_by(request):
    posts = BlogPost.Published.all()[:3]
    return render(
        request,
        'main/home.html',
        {'posts':posts}
    )
    
