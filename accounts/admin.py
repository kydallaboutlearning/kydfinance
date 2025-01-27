from django.contrib import admin
from .models import Profile
from parler.admin import TranslatableAdmin


@admin.register(Profile)
class ProfileModel(TranslatableAdmin):
    list_display = ['user', 'date_of_birth', 'phone_number', 'display_bio', 'created', 'last_login']
    list_editable = ['phone_number']  # Ensure this is in list_display
    search_fields = ['user__username', 'user__email', 'phone_number']  # Add search functionality
    list_filter = ['created', 'last_login']  # Filters for admin panel

    def display_bio(self, obj):
        """Display the translated bio in the list view."""
        return obj.bio  # Parler handles translations automatically
    display_bio.short_description = 'Bio'  # Admin column title
