from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import RegistrationForm
from django.contrib import messages

from django.contrib.auth.models import User


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

# Create your views here.
# views for dashboard
@login_required
def DashboardView(request):
    # Adding user profile
    UserProfile = Profile.objects.get(user=request.user)
    
    return render(request,'main/dashboard.html', {'Userprofile': UserProfile})


# creating a registration view
def register_view(request):

    # GETTING from post request
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        # checking if form is valid
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            username = form.cleaned_data.get('username')

        

            # Create the user
            user = User.objects.create(
                username=username,
                email=email,
                password=make_password(password),
            )
            messages.success(request,f"Congrats,{user.username}. Your account has been created successfully")

            return redirect("accounts:login")  # Redirect to login after registration
        else:
            messages.error(request,'Pls, correct the error below')
            form = RegistrationForm()
            
    else:
        form = RegistrationForm()

    return render(request, "registration/register.html", {"form": form})




def LogoutView(request):
    return render(request,'registration/logoutform.html')


