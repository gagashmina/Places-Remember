from django.db import models

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()


class Place(models.Model):
    place_name = models.CharField(max_length=50)
    content = models.TextField()
    time_create = models.TimeField(auto_now=False, auto_now_add=True)

    
    def __str__(self) -> str:
        return self.place_name