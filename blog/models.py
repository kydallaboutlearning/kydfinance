
from django.db import models
from django.utils import timezone
from parler.models import TranslatableModel, TranslatedFields




# creating models
class BlogPost(TranslatableModel):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    # Fields that are not translatable
    slug = models.SlugField(max_length=250)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )

    # Translatable fields
    translations = TranslatedFields(
        title = models.CharField(max_length=250),
        body = models.TextField(),
    )

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

