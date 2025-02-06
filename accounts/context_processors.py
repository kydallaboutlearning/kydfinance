from .models import Profile




from .models import Profile

def user_profile(request):
    """Context processor to make the user's profile available in all templates."""
    if request.user.is_authenticated:  # Ensure user is logged in
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            profile = None  # If profile doesn't exist, return None
    else:
        profile = None  # If user is not logged in, return None

    return {"profile": profile}
