from .models import *
from django import forms

class SubsriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('name','email')

        widgets = {
                   'name' : forms.TextInput(attrs={'class':'form-control','id':"hisname",'value':""}),
                   'email': forms.TextInput(attrs={'class':'form-control', 'autocomplete':'on','value':"",'id':"hisemail"}),

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
        if Subscriber.objects.filter(email=email).count() > 0:
              raise forms.ValidationError("We have a user with this user email-id")
 
        return email
