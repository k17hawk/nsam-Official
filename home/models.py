from django.db import models

# Create your models here.
class SlideImage(models.Model):
    image_id=models.AutoField(primary_key = True)
    Heading=models.CharField(max_length=60)
    description=models.CharField(max_length=200)
    image = models.ImageField(upload_to='home/image')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
    def __str__(self):
        return self.Heading

class Subscriber(models.Model):
    id= models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
         ordering = ['-date']
    def  __str__(self):
           return self.name
        