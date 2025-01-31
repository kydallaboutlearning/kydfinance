from django.shortcuts import render
from .models import BlogPost
from django.views.generic import ListView, DetailView

# Create your views here.

def post_list_by(request):
    posts = BlogPost.Published.all()[:3]
    return render(
        request,
        'main/home.html',
        {'posts':posts}
    )
    
class Post_list(ListView):
    """Adding a general page view"""
    model = BlogPost()
    query_set = BlogPost.Published.all()
    paginate_by = 5
    context_object_name = 'posts'    

    
