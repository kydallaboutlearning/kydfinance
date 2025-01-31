from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import BlogPost


# Register your models here.
@admin.register(BlogPost)
class BlogAdmin(TranslatableAdmin):
    list_display = ['safe_title', 'status', 'publish', 'created']  # FIXED: Using safe_title
    list_editable = ['status']
    search_fields = ['translations__title', 'status', 'publish']  # FIXED: Parler requires translations__
    date_hierarchy = 'publish'  # FIXED TYPO
    ordering = ('status', '-publish')  # FIXED: Using a tuple

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}
