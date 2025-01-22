from django.db import models
from django.contrib.auth  import get_user_model
import timezone



# Create your models here.c

class ProfileModel(models.model):
     user = get_user_model()
     User = models.ForeignKey(model=user, on_delete=models.CASCADE)
     age = models.PositiveIntegerField()
     last_logged_in = models.DateTimeField(auto_now=timezone.now())