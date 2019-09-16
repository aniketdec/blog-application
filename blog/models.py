from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import *
from users.models import Profile
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    posted_on=models.DateTimeField(default=timezone.now)
    author=models.IntegerField()
    #avatar=models.ImageField(null=True)
    likes=models.ManyToManyField(User, related_name='liked', symmetrical=False)
    def __str__(self):
        return self.title
class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
