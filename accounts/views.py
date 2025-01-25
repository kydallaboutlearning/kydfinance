from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import RegistrationForm


from django.contrib.auth.models import User


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

# Create your views here.
# views for dashboard
@login_required
def DashboardView(request):
    # Adding user profile
    UserProfile = Profile
    
    return render(request,'main/dashboard.html', {'Userprofile': UserProfile})


# creating a registration view
def register_view(request):

    # GETTING from post request
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        # checking if form is valid
        if form.is_valid():
            identifier = form.cleaned_data.get("identifier")
            password = form.cleaned_data.get("password")

            # Check if it's an email or username
            if "@" in identifier:  # Treat it as an email
                email = identifier
                username = email.split("@")[0]  # Generate a username from the email
            else:  # Treat it as a username
                username = identifier
                email = None

            # Create the user
            user = User.objects.create(
                username=username,
                email=email,
                password=make_password(password),
            )
            return redirect("login")  # Redirect to login after registration
    else:
        form = RegistrationForm()

    return render(request, "register.html", {"form": form})




def LogoutView(request):
    return render(request,'registration/logoutform.html')


