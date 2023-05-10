from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
Courses = get_user_model() 

# Create your models here.
class Profile(models.Model):
    username = models.TextField(max_length=20, default='username', primary_key=True)
    email = models.EmailField(default='user@email.com')
    password = models.CharField(default='********', max_length=20)
    password_2 = models.CharField(default='********', max_length=20)

#General Course Models
class Course(models.Model):
    code = models.CharField(max_length=10, default='CSC 217', primary_key=True)
    title = models.TextField(max_length=50, default='Discrete Mathemantics')
    desc = models.TextField(max_length=500, default='')
    