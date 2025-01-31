from django.db import models
from django.utils import timezone
from parler.models import TranslatableModel, TranslatedFields
from parler.managers import TranslatableManager  # Import Parler's Manager
from django.contrib.auth import get_user_model

# Creating a model manager that supports translations
class PublishedManager(TranslatableManager):  # FIXED: Inherit from TranslatableManager
    def get_queryset(self):
        return super().get_queryset().filter(status=BlogPost.Status.PUBLISHED)

# Creating BlogPost model
class BlogPost(TranslatableModel):
    user = get_user_model()
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    # Fields that are not translatable
    author = models.ForeignKey(
                                user,
                                on_delete = models.CASCADE,
                                related_name = 'blog_posts'
                               ) 
    slug = models.SlugField(max_length=250, unique=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to = 'blogs/%Y/%m/%d', 
                              blank = True,null = True)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,  # FIXED: Added .choices
        default=Status.DRAFT
    )

    # Translatable fields
    translations = TranslatedFields(
        title=models.CharField(max_length=250),
        body=models.TextField(),
    )
    
    # Registering model managers
    objects = TranslatableManager()  # Default manager for Parler
    published = PublishedManager()  # Custom manager for published posts

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.safe_translation_getter('title', default='[No Title]')  # FIXED: Safe fallback for missing translations
