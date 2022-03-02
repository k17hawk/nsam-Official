from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


class PublicHealth(models.Model):
    healthId = models.AutoField(primary_key = True)
    title = models.CharField(max_length=200)
    description = RichTextUploadingField()
    date_And_time = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='PublicHealth/picture', default="",null=True,blank=True)
    class Meta:
        ordering = ["date_And_time"]
    def __str__(self):
        return self.title

class EducationAwarness(models.Model):
    eduId = models.AutoField(primary_key = True)
    title = models.CharField(max_length=200)
    description = RichTextUploadingField()
    picture = models.ImageField(upload_to='EducationAwarness/picture', default="",null=True,blank=True)
    date_And_time = models.DateTimeField(auto_now_add=True)
    #objects = PostManager()
    class Meta:
        ordering = ["date_And_time"]
    def __str__(self):
        return self.title

class Workshop(models.Model):
    workshopId = models.AutoField(primary_key = True)
    title = models.CharField(max_length=200)
    description = RichTextUploadingField()
    date_And_time = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='Workshop/picture', default="",null=True,blank=True)
    #objects = PostManager()
    class Meta:
        ordering = ["date_And_time"]
    def __str__(self):
        return self.title

class wildlife(models.Model):
    disId = models.AutoField(primary_key = True)
    title = models.CharField(max_length=200)
    description = RichTextUploadingField()
    date_And_time = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='wildlife/picture', default="",null=True,blank=True)
    #objects = PostManager()
    class Meta:
        ordering = ["date_And_time"]
    def __str__(self):
        return self.title
