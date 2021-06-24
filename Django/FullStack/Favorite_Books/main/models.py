from datetime import date
from django.db import models
from django.db.models.deletion import CASCADE
import re
from django.db.models.fields.related import ForeignKey
from django.db.models.fields.reverse_related import ManyToManyRel
import bcrypt
# Create your models here.
class TableManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['fn']) < 2:
            errors['fn'] = "First Name must at least  be 2 characters"
        if len(postData['ln']) < 2:
            errors['ln'] = "Last Name must at least  be 2 characters"
        if not EMAIL_REGEX.match(postData['email']):          
            errors['email'] = "Invalid email address!"
        elif len(User.objects.filter(email=postData['email'])) > 0:
            errors['email'] = "This email is taken"
        if len(postData['pwd']) < 8:
            errors['pwd'] = "Password must be at least 8 characters"
        elif postData['pwd'] != postData['cpwd']:
            errors['pwd'] = "Passwords don't match"
        return errors

    def login_validator(self, postData):
        errors = {}
        email = User.objects.filter(email = postData['email'])
        if email:
            this = email[0] 
            if not bcrypt.checkpw(postData['pwd'].encode(), this.password.encode()):
                errors['un'] = "Invalid login credentials"
        else:
            errors['un'] = "Invalid login credentials"
        return errors

    def book_valiadtor(self,postData):
        errors = {}
        if len(postData['title']) < 1:
            errors['title'] = "A title is required"
        if len(postData['desc']) < 5 :
            errors['desc'] = "A description must be at least 5 characters"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TableManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name='books',on_delete = models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name='liked_books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TableManager()