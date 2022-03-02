from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    publishBy=models.CharField(max_length=100,blank=True,null=True)
    Blog_by = models.CharField(max_length=50,null=True,blank=True)
    title = models.CharField(max_length=150, default="")
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='Blog/images', null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title 