from accounts.models import Profile


def create_profile(backend, user, *args, **kwargs):
 """
 Create user profile for social authentication
 """
 Profile.objects.get_or_create(user=user)