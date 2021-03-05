from django.db import models
from stdimage import StdImageField

# Create your models here.    


class Work(models.Model):

  title = models.CharField(max_length=250)
  # image = models.ImageField(upload_to='img/upload', null= True ,blank=True)
  image = StdImageField(upload_to='img/upload', null= True ,blank=True)

  url = models.URLField(blank=True)
  date = models.TextField(max_length=50)
  partner = models.CharField(max_length=250)
  content = models.CharField(max_length=400)

  def __str__(self):
    return self.title

class Blog(models.Model):

  title = models.CharField(max_length=250)
  url = models.URLField(blank=True)
  date = models.TextField(max_length=50)
  category = models.CharField(max_length=50)

  def __str__(self):
    return self.title

