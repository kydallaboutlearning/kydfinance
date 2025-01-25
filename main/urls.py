from django.urls import path,include
from django.utils.translation import gettext_lazy as _
from .views import LandingPageView,DashboardView


# URL patterns for the main app
app_name = 'main'


# setting up the URL patterns
urlpatterns = [
     path('', LandingPageView, name='landing-page'),
     path(_('Accounts/'),include('django.contrib.auth.urls'),
     path( _('DashBoard/'),DashboardView, name = 'dashboard')),
    ]