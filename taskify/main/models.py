from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    fullName = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100,unique=True)
    profession = models.CharField(max_length = 200)
    profilePhoto = models.ImageField(upload_to='userProfilePhoto',blank=True,null=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.username


class Tasks(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)    
    Title = models.CharField(max_length=50)
    dueDate = models.DateField()
    Description = models.TextField(null=True,blank=True)
    priority = models.IntegerField()
    completeStatus = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
