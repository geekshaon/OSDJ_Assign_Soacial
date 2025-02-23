from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='files/posts/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.content[:20]} - {self.user.username}'
