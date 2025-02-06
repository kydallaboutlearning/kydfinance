# importing for list and detail view
from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.views.generic import ListView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.decorators.http import require_POST

# Create your views here.

def post_list_norms(request):
    post_list = BlogPost.published.all()
    # Pagination with 10 posts per page
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer get the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range get last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                     'blog/post/list.html', 
                     {'posts': posts, 'page_obj': posts}
                     )

        
   

    

# creating the class post view
class Post_list(ListView):
    """Adding a general page view"""
    model = BlogPost()
    query_set = BlogPost.published.all()
    paginate_by = 5
    context_object_name = 'posts'    


def Post_Detail(request,id,year,month,day,post):
    # get the post based on the requested data in frm of year, day,
    post = get_object_or_404(
        BlogPost,
        status=BlogPost.Status.PUBLISHED,
        id = id,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    ) 
    
    return render(request, 'blog/post/detail.html', {'post': post})




@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(
         BlogPost,
        status=BlogPost.Status.PUBLISHED,
        id = id,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    comment = None
    # A comment was posted
    form = CommentForm(data=request.POST)
    if form.is_valid():
        # Create a Comment object without saving it to the database
        comment = form.save(commit=False)
        # Assign the post to the comment
        comment.post = post
        # Save the comment to the database
        comment.save()
    return render(
        request,
        'blog/post/comment.html',
        {
            'post': post,
            'form': form,
            'comment': comment
        },
    )
    
    
