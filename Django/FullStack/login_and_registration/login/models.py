from django.db import models
# import re
# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        email_in_db = User.objects.filter(email = postData['email'])
        # add keys and values to errors dictionary for each invalid field
        if len(postData['fname']) < 2:
            errors["fname"] = "First Name should be at least 2 characters"
        if len(postData['lname']) < 2:
            errors["lname"] = "Last Name should be at least 2 characters"
        if len(postData['pwd']) < 8:
            errors["pwd"] = "Passowrd should be at least 8 characters"
        if postData['pwd'] != postData['cpwd'] :
            errors["pwd"] = "Confirm Password should match Password"
        if email_in_db:
            errors['email'] = "This email is already used"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=70)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()