from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission



class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Tour(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='Tour_Images/',  null=True, blank=True)
    season_start = models.DateField(null=True, blank=True)
    season_end = models.DateField(null=True, blank=True)
    mainstream= models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True, null=True, blank=True)
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_user_set')



class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    num_people = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15)
