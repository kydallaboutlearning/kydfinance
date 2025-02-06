from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import BlogPost, Comment
from django.utils.translation import gettext_lazy as _

# Register your models here.
@admin.register(BlogPost)
class BlogAdmin(TranslatableAdmin):
    list_display = ['title', 'author','status', 'publish', 'created','updated'] # Use get_title instead of 'safe_title'
    list_editable = ['status','author']
    search_fields = ['translations__title', 'status', 'publish']  #Use translations__title for search
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    show_facets = admin.ShowFacets.ALWAYS
    
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}

    
    
    def get_title(self, obj):
        return obj.safe_translation_getter('title', default='[No Title]')  #  Fallback for missing translations
    
    get_title.short_description = 'title'  # Set column header in admin panel



@admin.register(Comment)
class CommentAdmin(TranslatableAdmin):
    list_display = ('profile', 'post', 'get_translated_body', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('translations__body',)
    ordering = ('-created',)

    def get_translated_body(self, obj):
        return obj.safe_translation_getter("body", default=_("[No Body]"))
    get_translated_body.short_description = _("Comment Body")

