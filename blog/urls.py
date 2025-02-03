from django.urls import path
from django.utils.translation import gettext_lazy as _
from .views import *

                    

# URL patterns for the main app
app_name = 'blog'


# setting up the URL patterns
urlpattern = [
     path('', post_list_norms, name ='post_list'),
     path('post_class/', Post_list.as_view(), name = 'post_list_class'),
     path(
        '<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.post_detail,
        name='post_detail',
          ),
     
     ]