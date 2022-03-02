from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

'''
class About(models.Model):
    abtId = models.AutoField(primary_key = True)
    description = RichTextUploadingField()
    date_And_time = models.DateTimeField(auto_now_add=True)
    #objects = PostManager()
    class Meta:
        ordering = ["date_And_time"] 
  '''
class OurTeam(models.Model):
    teamId = models.AutoField(primary_key=True)
    TypeOfMember = models.CharField(max_length=150)
    Full_Name = models.CharField(max_length=50)
    facebookId = models.URLField(max_length=50,null=True,blank=True)
    instagramId = models.URLField(max_length=50,null=True,blank=True)
    linkedIn = models.URLField(max_length=50,null=True,blank=True)
    Image = models.ImageField(upload_to='About/Team')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.TypeOfMember
    class Meta:
        ordering = ['-date','TypeOfMember']     



class Advisor(models.Model):
    advisorId = models.AutoField(primary_key=True)
    Full_Name = models.CharField(max_length=50)
    facebookId = models.URLField(max_length=50,null=True,blank=True)
    instagramId = models.URLField(max_length=50,null=True,blank=True)
    linkedIn = models.URLField(max_length=50,null=True,blank=True)
    Image = models.ImageField(upload_to='About/Advisor')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Full_Name
    class Meta:
        ordering = ['-date','Full_Name']    



class Donars_and_partners(models.Model):
    id = models.AutoField(primary_key = True)
    Title= models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
    	ordering = ['-date']
    

    def __str__(self):
        return self.Title



    
     

class Image_multiple_Donar(models.Model):
	Image = models.ForeignKey(Donars_and_partners,on_delete=models.CASCADE)
	image = models.ImageField(upload_to='Donars/image')
	date = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=False)
	class Meta:
		ordering = ['-date']
    
	def __str__(self):
		return self.Image.Title

