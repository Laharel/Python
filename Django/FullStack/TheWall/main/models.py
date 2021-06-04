from datetime import date, datetime
from django.contrib import messages
from django.db import models
import re

# Create your models here.
class WallManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        email_in_db = User.objects.filter(email=postData['email'])
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['fn']) <3:
            errors['fn'] = "First Name can't be less than 3 characters"
        if len(postData['ln']) <3:
            errors['ln'] = "Last Name can't be less than 3 characters"
        if not EMAIL_REGEX.match(postData['email']):          
            errors['email'] = "Invalid email address!"
        if email_in_db:
            errors['email'] = "This Email is already used"
        if len(postData['pwd']) <8:
            errors['pwd'] = "Password can't be less than 8 characters"
        if postData['pwd'] != postData['cpwd'] :
            errors['cpwd'] = "Confirm Password must match Password"
        return errors

    def message_validator(self, postData):
        errors = {}
        if len(postData['msg']) == 0:
            errors['msg'] = "Message can't be empty"
        return errors

    def comment_validator(self, postData):
        errors = {}
        if len(postData['cmt']) == 0:
            errors['cmt'] = "Comment can't be empty"
        return errors



class User(models.Model):
    fn = models.CharField(max_length=30)
    ln = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    pwd = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WallManager()

class Message(models.Model):
    message = models.TextField()
    date = models.DateField(default=datetime.today())
    user = models.ForeignKey(User, related_name="posts", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WallManager()

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, related_name="comments",on_delete=models.CASCADE)
    post = models.ForeignKey(Message, related_name="comments",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WallManager()