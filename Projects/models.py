from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


class Completed(models.Model):
    Id = models.AutoField(primary_key = True)
    Heading = models.CharField(max_length=200)
    Project_Leader = models.CharField(max_length=30,null=True,blank=True)
    Location = models.CharField(max_length=30,null=True,blank=True)
    Funding_Agency = models.CharField(max_length=50,null=True,blank=True)
    Description = RichTextUploadingField()
    date_And_time = models.DateTimeField(auto_now_add=True)
    Picture = models.ImageField(upload_to='Project/Completed', default="",null=True,blank=True)
    class Meta:
        ordering = ["date_And_time"]
    def __str__(self): 
        return self.Heading


class Ongoing(models.Model):
    Id = models.AutoField(primary_key = True)
    Heading = models.CharField(max_length=200)
    Project_Leader = models.CharField(max_length=30,null=True,blank=True)
    Location = models.CharField(max_length=30,null=True,blank=True)
    Funding_Agency = models.CharField(max_length=50,null=True,blank=True)
    Description = RichTextUploadingField()
    date_And_time = models.DateTimeField(auto_now_add=True)
    Picture = models.ImageField(upload_to='Project/Ongoing', default="",null=True,blank=True)
    class Meta:
        ordering = ["date_And_time"]
    def __str__(self):
        return self.Heading

