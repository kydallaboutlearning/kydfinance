from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import BlogPost



# Register your models here.
@admin.register(BlogPost)
class BlogAdmin(TranslatableAdmin):
    list_display = ['title','status','publish','created']

    
    
    
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}
    
    