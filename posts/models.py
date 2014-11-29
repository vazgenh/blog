from django.db import models
from authors.models import Author
# Create your models here.
class Post(models.Model):
    post_author = models.ForeignKey(Author)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)

