from django.db import models
from django.contrib.auth import get_user_model
from parler.models import TranslatableModel, TranslatedField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


User = get_user_model()

class Profile(TranslatableModel):

     translations = TranslatedField(
            Bio = models.TextField(blank=True),
            financial_goal = models.TextField(blank=True)
     )
     user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='Profile')
     profile_pics = models.ImageField(
                         upload_to='users/%Y/%m/%d/',
                         blank=True
                         )
     Age = models.DateField(
          blank=True, null=True
     )
     
     phone_number = PhoneNumberField(blank = True)

   