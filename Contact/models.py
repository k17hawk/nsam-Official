from django.db import models
from ckeditor.fields import RichTextField
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    Message = RichTextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
    def __str__(self):
        return self.name
