from django.urls import path,include
from django.utils.translation import gettext_lazy as _
from .views import DashboardView, register_view

                    

# URL patterns for the main app
app_name = 'accounts'


# setting up the URL patterns
urlpatterns = [
    path('', include('django.contrib.auth.urls')),  
    path(_('DashBoard/'), DashboardView, name='dashboard'),  
    path(_('register/'), register_view, name='register'),
]
     