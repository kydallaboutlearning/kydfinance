# importing for list and detail view
from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.views.generic import ListView
from django.core.paginator import 

# Create your views here.

def post_list_norms(request):
    posts = BlogPost.published.all()
        
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )

    

# creating the class post view
class Post_list(ListView):
    """Adding a general page view"""
    model = BlogPost()
    query_set = BlogPost.published.all()
    paginate_by = 5
    context_object_name = 'posts'    


def Post_Detail(request,year,month,day,post):
    # get the post based on the requested data in frm of year, day,
    post = get_object_or_404(
        BlogPost,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    
    
