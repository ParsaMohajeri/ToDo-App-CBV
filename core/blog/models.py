# import part
from django.db import models
from django.contrib.auth import get_user_model
# ____________________________________________________________________________________________________
# Create your models here.

User = get_user_model()
# getting user

class Post(models.Model):
    """
    this is a shape of our posts
    """
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField()
    title=models.CharField(max_length=30)
    content=models.TextField(max_length=250)
    status=models.BooleanField(default=False)
    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)
    published_date=models.DateTimeField(null=True,blank=True)


    def __str__(self):
        return self.title

