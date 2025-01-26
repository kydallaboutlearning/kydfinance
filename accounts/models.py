from django.db import models

from django.contrib.auth import get_user_model
from parler.models import TranslatableModel, TranslatedFields
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


User = get_user_model()

class Profile(TranslatableModel):

     translations = TranslatedFields(
            bio = models.TextField(blank=True),
            financial_goal = models.TextField(blank=True)
     )
     user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='Profile')
     profile_pics = models.ImageField(
                         upload_to='users/%Y/%m/%d/',
                         blank=True
                         )
     date_of_birth = models.DateField(
          blank=True, null=True
     )
     created = models.DateTimeField(auto_now_add = True)
     last_login = models.DateTimeField(auto_now = True)
     
     phone_number = PhoneNumberField(blank = True)

     def  __str__(self):
          return f"Profile of {self.user.username}"


   