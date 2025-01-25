from django.shortcuts import render
from django.utils.translation import get_language
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.


def LandingPageView(request):
    current_language = get_language()

    context = {
        'current_language': current_language
    }
    return render(request, 'main/home.html', context)


# views for dashboard
@login_required
def DashboardView(request):
    # Adding user profile
    UserProfile = Profile
    
    return render(request,'main/dashboard.html', {'Userprofile': UserProfile})



