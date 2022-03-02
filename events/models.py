from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import Q



class New(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=50)
    description = RichTextUploadingField()
    date = models.DateTimeField()
    location=models.CharField(max_length=50 ,blank=True,null=True)
    picture = models.ImageField(upload_to='New/picture',null=True,blank=True)
    active = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["-date"]
    def __str__(self):
        return self.title
