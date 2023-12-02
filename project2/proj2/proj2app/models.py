from django.db import models


# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='Images')
    desc = models.TextField()

    def __str__(self):
        return self.name

class profile(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='Images')
    desc = models.TextField()
    def __str__(self):
        return self.name