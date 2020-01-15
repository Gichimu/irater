from django.db import models
# from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Profile(models.Model):
    avatar = models.ImageField(upload_to='images')
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

class Project(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    photo = models.ImageField(upload_to='images')
    link = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Rating(models.Model):
    post = models.ForeignKey(Project, on_delete=models.CASCADE, default='')
    usability = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    design = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    content = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    avg = models.IntegerField(default=0)

    def __str__(self):
        return self.usability




