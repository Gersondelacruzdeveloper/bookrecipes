from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Recepes(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=201, null=True)
    image = models.ImageField(upload_to='uploads/', null=True)
    method = RichTextUploadingField(null=True, blank=True)
    service_size = models.IntegerField(null=True, blank=True)
    cooking_time = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    calories = models.CharField(max_length=201, null=True, blank=True)
    fat = models.CharField(max_length=201, null=True, blank=True)
    protein = models.CharField(max_length=201, null=True, blank=True)
    fibre = models.CharField( max_length=201, null=True, blank=True)
    carbohidrates = models.CharField(max_length=201, null=True, blank=True)
    salt = models.CharField(max_length=201, null=True, blank=True)


    def __str__(self):
        return str(self.title)


class Review(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True,)
    content = models.TextField(null=True, blank=True,)
    recipes = models.ForeignKey(Recepes, on_delete=models.CASCADE, null=True, blank=True, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title