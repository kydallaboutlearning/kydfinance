from django.db import models
from django.utils import timezone
from parler.models import TranslatableModel, TranslatedFields
from parler.managers import TranslatableManager  # Import Parler's Manager

# Creating a model manager that supports translations
class PublishedManager(TranslatableManager):  # FIXED: Inherit from TranslatableManager
    def get_queryset(self):
        return super().get_queryset().filter(status=BlogPost.Status.PUBLISHED)

# Creating BlogPost model
class BlogPost(TranslatableModel):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    # Fields that are not translatable
    slug = models.SlugField(max_length=250, unique=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
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
