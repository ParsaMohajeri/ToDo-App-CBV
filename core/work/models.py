
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    """
    This defines the structure of our posts.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tasks/',null=True, blank=True)
    title = models.CharField(max_length=30)
    is_done = models.BooleanField(default=False)
    content = models.TextField(max_length=250)
    status = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    published_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
