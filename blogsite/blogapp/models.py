from django.db import models
from django.urls import reverse

# Create your models here.

class Author(models.Model):
    author_id = models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_id = models.EmailField()

    def __str__(self) -> str:
        return f"{self.first_name.title()} {self.last_name.title()}"


class BlogContent(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=99)
    blog_content = models.TextField()

    def __str__(self) -> str:
        return f"{self.blog_title} - {self.author.first_name.title()} {self.author.last_name.title()}"
    
    def get_absolute_url(self):
        return reverse("blogpage")
    

