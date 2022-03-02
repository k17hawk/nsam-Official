from django.db import models
from embed_video.fields import EmbedVideoField
import os
import uuid



# Create your models here.
def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return os.path.join("files", filename)


class Report(models.Model):
    resource_id = models.AutoField(primary_key = True)
    file = models.FileField(upload_to=user_directory_path, null=True)
    Heading= models.CharField(max_length=200)
    publicationYear = models.DateTimeField()
    date = models.DateTimeField(auto_now_add=True)
  
    class Meta:
    	ordering = ['-date']
    

    def __str__(self):
        return self.Heading



    
     

class Image_Resource(models.Model):
      imageId = models.AutoField(primary_key = True)
      title = models.CharField(max_length=100)  
      date = models.DateTimeField(auto_now_add=True)
      class Meta:
        ordering = ['-date']

      def __str__(self):
        return self.title

class Image_multiple(models.Model):
	Image = models.ForeignKey(Image_Resource,on_delete=models.CASCADE)
	image = models.ImageField(upload_to='resource/image')
	date = models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering = ['-date']
    
	def __str__(self):
		return self.Image.title
	

 

class Resource_Video(models.Model):
    video = EmbedVideoField()
    title = models.CharField(max_length=60)
    date = models.DateTimeField(auto_now_add=True)
    video_id = models.AutoField(primary_key=True)
    class Meta:
        ordering = ['-date']

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title    


class Poster_Resource(models.Model):
      PosterId = models.AutoField(primary_key = True)
      title = models.CharField(max_length=100)  
      date = models.DateTimeField(auto_now_add=True)
      class Meta:
        ordering = ['-date']

      def __str__(self):
        return self.title

class Poster_multiple(models.Model):
	Poster = models.ForeignKey(Poster_Resource,on_delete=models.CASCADE)
	poster = models.ImageField(upload_to='resource/Poster')
	date = models.DateTimeField(auto_now_add=True) 
	class Meta:
		ordering = ['-date']
	def __str__(self):
		return self.Poster.title        