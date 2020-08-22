from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField()
    img = models.ImageField()
    dataCreat = models.DateTimeField()
    category = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title