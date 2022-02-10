from django.db import models
class mode(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='xxx')
    category = models.CharField(max_length=50)


    def __str__(self):
        return self.name

# Create your models here.
