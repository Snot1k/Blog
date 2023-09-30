from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=25)

class Post(models.Model):
    post_header = models.CharField(max_length=50)
    post_text = models.TextField()
    author = models.CharField(max_length=50)
    datetime = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default="no category")

    def get_absolute_url(self):
        return reverse("post-details", args=[str(self.id)])