from django.db import models

# Create your models here.


class Profile(models.Model):
    title = models.CharField(max_length=50)
    discription = models.TextField(max_length=900)
    image = models.ImageField(upload_to='portfolio/image/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Profiles(models.Model):
    title = models.CharField(max_length=50)
    discription = models.TextField(max_length=900)
    image = models.ImageField(upload_to='portfolio/image/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
