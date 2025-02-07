# importing for list and detail view
from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.views.generic import ListView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from .models import Comment
from .forms import CommentForm
from django.utils.translation import getext_lazy as _
from django.contrib import messages
from django.urls import reverse
from .forms import *
# importing requirements for sending email
from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings





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


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import BlogPost, Profile, Comment
from .forms import CommentForm
from django.utils.translation import gettext as _

def Post_Detail(request, id, year, month, day, post):
    # Retrieve the post
    post = get_object_or_404(
        BlogPost,
        status=BlogPost.Status.PUBLISHED,
        id=id,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )

    # Get the latest 5 active comments
    comments = post.comments.filter(active=True)[:5]
    
    # Translate comment body text
    for comment in comments:
        comment.translated_body = comment.safe_translation_getter("body", default=_("[No Body]"))

    # Initialize the comment form
    commentform = CommentForm()

    if request.method == "POST":
        commentform = CommentForm(data=request.POST)
        
        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
            except Profile.DoesNotExist:
                profile = None  # Profile doesn't exist

            if commentform.is_valid():
                # Save the comment
                comment = commentform.save(commit=False)
                comment.post = post  # Assign post
                comment.profile = profile  # Assign user profile
                comment.save()
                
                messages.success(request, "Your comment has been posted!")
                return redirect(request.path)  # Refresh the page

        else:
            messages.error(request, "Sorry, you need to log in or create an account to comment.")
            return redirect("accounts:login")

    return render(
        request,
        "blog/post/detail.html",
        {"post": post, "comments": comments, "commentform": commentform},
    )

def comment_view(request,post_id,year,month,day,post):
    post = get_object_or_404(
        BlogPost,
        status=BlogPost.Status.PUBLISHED,
        id = post_id,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )  
    comments = post.comments.filter(active=True)
    return render(
        request,'blog/post/comments/list.html',{'post':post,'comments':comments,}
    )


def post_share(request,post_id,year,month,day,post):
    # getting the postvia it's
     post = get_object_or_404(
        BlogPost,
        id = post_id,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    ) 
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(data=request.POST)
        if form.is_valid()
            cd = form.cleaned_data
            post_url= request.build_absolute_uri(
                 post.get_absolute_url()
            ) #getting the url of the post to  be shared

            email_subject = (f"{cd['name']} ({cd['email']}) "
                             f"recommends you read {post.title}"
                             )
            email_body = render_to_string('blog/share-email.html',{'cd':cd,'post_url',post_url})
            email = EmailMultiAlternatives(email_subject, "",cd['email'], cd['to'])
            email.attach_alternative(email_body,'text/html')
            email.send()
            sent =True
            messages.success(request, _(f"You have succesfully sent the email to {cd['to']}."))
        else:
            form = EmailPostForm()

    return render(
            request,
            'blog/post/share.html',
             {
        'post': post,
        'form': form,
            'sent': sent
            }
        )








    
    
