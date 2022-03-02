from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Contact
from django.core.validators import validate_email
from django.core.validators import RegexValidator
import re

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email','phone', 'Message')
      
        widgets = {
                   'name' : forms.TextInput(attrs={'class':'form-control','id':"hisname",'value':""}),
                   'email': forms.TextInput(attrs={'class':'form-control', 'autocomplete':'on','value':"",'id':"hisemail"}),
                   'phone': forms.TextInput(attrs={'class': "form-control",'id':"hisphone",'value':""}),
                   'Message': RichTextWidget(attrs={'class':'form-control', 'autocomplete':'off','value':"",'id':"hiscontent"})
        }

    def clean_name(self):
        name = self.cleaned_data["name"]
        MIN_LENGTH = 9
        MAX_LENGTH  = 25
        if  name.isnumeric():
            raise forms.ValidationError("Name cannot be Numeric")

        else:
            if len(name) < MIN_LENGTH :
                raise forms.ValidationError("Please enter full name")
            else:
                if len(name) > MAX_LENGTH:
                    raise forms.ValidationError("Name is to long")
        return name


    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
             emdd=validate_email(email)
        except:
             return forms.ValidationError("Email is not in correct format")
        return email

    def clean_phone(self):
      phone = self.cleaned_data["phone"]
      match = re.search(r'(^[+0-9]{1,3})*([0-9]{10,11}$)',phone)
      if not match:
              raise forms.ValidationError("Phone number is incorrect")
      else:
            if len(phone) > 15:
                  raise forms.ValidationError("Phone number is To Long")

      return phone

    def clean_Message(self):
      message = self.cleaned_data["Message"]
      MIN_LENGTH = 50
      if len(message) < 50 :
              raise forms.ValidationError("Message must have %d words" %MIN_LENGTH)
      return message
