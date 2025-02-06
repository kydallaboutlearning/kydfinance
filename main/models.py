from django.db import models


# creating models for newsletter:
class Newsletter(models.Model):
    email = models.EmailField(blank=True)