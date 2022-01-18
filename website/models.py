from django.db import models

class Highlights(models.Model):
    img = models.ImageField(upload_to='highlights/')

class Gallery(models.Model):
    img = models.ImageField()
