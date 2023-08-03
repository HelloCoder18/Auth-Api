from django.db import models
# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    desc = models.TextField(max_length=1000)
    date=models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title