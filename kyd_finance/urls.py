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


# imporrting requirements for internalization
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect









# Add internationalized URL patterns
urlpatterns = (
    path('admin/', admin.site.urls),
    path(('rosetta/'), include('rosetta.urls')),
    path('',include('main.urls',namespace='main'))
)


