from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import BlogPost

# Register your models here.
@admin.register(BlogPost)
class BlogAdmin(TranslatableAdmin):
    list_display = ['get_title', 'status', 'publish', 'created'] # Use get_title instead of 'safe_title'
    list_editable = ['status']
    search_fields = ['translations__title', 'status', 'publish']  #Use translations__title for search
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    
    def get_title(self, obj):
        return obj.safe_translation_getter('title', default='[No Title]')  #  Fallback for missing translations
    
    get_title.short_description = 'Title'  # Set column header in admin panel
