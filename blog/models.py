from django.db import models
from django.utils import timezone
from parler.models import TranslatableModel, TranslatedFields
from parler.managers import TranslatableManager
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone



# Custom manager for published posts
class PublishedManager(TranslatableManager):
    def get_queryset(self):
        return super().get_queryset().filter(status=BlogPost.Status.PUBLISHED)

# BlogPost model
class BlogPost(TranslatableModel):
    User = get_user_model()  
    
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    # Fields that are not translatable
        # Translatable fields
    translations = TranslatedFields(
        title=models.CharField(max_length=250),
        body=models.TextField(),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts",
        null=True,  #  Allow existing records to have no author
        blank=True  #  Optional field
    )
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="blogs/%Y/%m/%d", blank=True, null=True)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT
    )



    # Registering model managers
    objects = TranslatableManager()  # Default manager
    published = PublishedManager()  # Custom manager for published posts

    class Meta:
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"]),
        ]
        
        
    # getting the translation

    def __str__(self):
        return self.safe_translation_getter("title", default="[No Title]")
    
    def get_translated_title(self):
        return self.safe_translation_getter("title", default="[No Title]")

    def get_translated_body(self):
        return self.safe_translation_getter("body", default="[No Body]")

    # function to get url fro the post detail
    def get_absolute_url(self):
        return reverse(
            'blog:post_detail',
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug,
            ],
        )