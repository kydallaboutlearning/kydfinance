from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import reverse,redirect,render
from .models import Profile
# Create your tests here.

class UseerAuthTest(TestCase):
     
     def setUp(self):
          # setting up the user
               User = get_user_model()

               self.username = 'testuser'
               self.email = 'testuseremail'
               self.password = 'testpassword'
               self.first_name = 'testfirstname'
               self.last_name = 'testlastname'
               self.user = User.objects.create_user(username=self.username, email=self.email ,password=self.password,first_name=self.first_name,last_name=self.last_name)
               



     def test_signUp(self):
          # setting up the user
          # asserting the logic for creating a user
          self.assertEqual(self.user.username, 'testuser')
          self.assertEqual(self.user.email, 'testuseremail')
          self.assertTrue(self.user.check_password('testpassword'))
          self.assertEqual(self.user.first_name, 'testfirstname')
          self.assertEqual(self.user.last_name, 'testlastname')
          self.assertFalse(self.user.check_password('wrongpassword'))
          self.assertTrue(self.user.is_active)
          self.assertFalse(self.user.is_staff)
          self.assertFalse(self.user.is_superuser)

           # Assert user exists in the database
          User = get_user_model()
          self.assertTrue(User.objects.filter(username='testuser').exists())

     def test_profile_created_on_user_creation(self):
        # Verify that the Profile was created by the signal
        profile_exists = Profile.objects.filter(user=self.user).exists()
        self.assertTrue(profile_exists, "Profile was not created when user was created.")


     
     def test_signin(self):

          # testing login
          login_successful = self.client.login(username='testuser', password='testpassword')
          self.assertTrue(login_successful)

          # login failed
          login_failed = self.client.login(username='testuser', password='wrongpassword')
          self.assertFalse(login_failed)

           #  Test login via POST request (valid credentials)
          response = self.client.post(reverse('accounts:login'), {
            "username": self.username,
            "password": self.password
        })


        # Test POST request to the login view with incorrect credentials
          response = self.client.post(reverse('accounts:login'), {
            "username": self.username,
            "password": "wrongpassword"
        })