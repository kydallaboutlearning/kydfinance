from django.urls import path
from django.utils.translation import gettext_lazy as _
from .views import *

                    

# URL patterns for the main app
app_name = 'blog'


# setting up the URL patterns
urlpatterns = [
     path('', post_list_norms, name ='post_list'),
     path(_('post_class/'), Post_list.as_view(), name = 'post_list_class'),
     path(_('<int:year>/<int:month>/<int:day>/<slug:post>/<int:id>/'), Post_Detail, name='post_detail'),
     path(_('/<int:post_id>/create_comment_on/<slug:post>'), post_comment, name='comment_form'),
     path(_('/<int:post_id>/comments_on/<slug:post>'), comment_view, name='comment_form'),

     ]