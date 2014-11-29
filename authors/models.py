from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
