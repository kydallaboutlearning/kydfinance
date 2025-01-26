"""
URL configuration for kyd_finance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


# imporrting requirements for internalization
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect


# Add internationalized URL patterns
urlpatterns = i18n_patterns(
    # django apps
    path('admin/', admin.site.urls),

    # third party  apps
    path('rosetta/', include('rosetta.urls')),

    # in apps
    path(_('account/'), include('accounts.urls', namespace='accounts')),
    # path('blog/', include('blog.urls', namespace='blog')),
    path('', include('main.urls', namespace='main')),
)
if settings.DEBUG:
    urlpatterns += static(
 settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
 )
