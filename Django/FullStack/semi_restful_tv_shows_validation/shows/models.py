from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        show = Show.objects.get(id=postData['show-id'])
        len_title = len(postData['title'])
        len_network = len(postData['network'])
        len_desc = len(postData['desc'])

        if len(postData['title']) < 2 and len_title != 0:
            errors['title'] = "Title should be at least two characters"
        if len(postData['network']) < 3 and len_network != 0:
            errors['network'] = "Network should be at least three characters"
        if len(postData['desc']) > 0 and len(postData['desc']) <10:
            errors['desc'] = "Description should be at least 10 characters or non"
        # if len(postData['release-date'] ==0):
        #     errors['release-date'] = "Release Date cannot be empty"

        return errors
# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

