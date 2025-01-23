from django.shortcuts import render
from django.utils.translation import get_language


# Create your views here.


def LandingPageView(request):
    current_language = get_language()

    context = {
        'current_language': current_language
    }
    return render(request, 'main/home.html', context)