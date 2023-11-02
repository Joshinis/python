from django import forms
from django.contrib.auth.models import User
from . import models


class AddorphanForm(forms.ModelForm):
    class Meta:
        model=models.Orphans
        fields=['Orphan_Name','DOB','Gender','Bgroup']



class AddoldageForm(forms.ModelForm):
    class Meta:
        model=models.Oldage
        fields=['Old_Name','DOB','Gender','Bgroup','Age']

class ContactForm(forms.ModelForm):
    class Meta:
        model=models.Contact
        fields=['user_Name','Email','message']



class AddexpenceForm(forms.ModelForm):
    class Meta:
        model=models.Expence
        fields=['Description','Bill_No','Bill_File','Amount','Type']
        


class AddassetsForm(forms.ModelForm):
    class Meta:
        model=models.Assets
        fields=['Description','Quantity','Cost','Type']

class AdddonationForm(forms.ModelForm):
    class Meta:
        model=models.Donation
        fields=['Amount','Type']   
class AddadoptionForm(forms.ModelForm):
    class Meta:
        model=models.Adoption
        fields=[]  

class ClientPaymentForm(forms.ModelForm):
    class Meta:
        model=models.Payment
        fields=['status','amount']    


class DonorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        

class ExtraForm(forms.ModelForm):
    class Meta:
        model=models.Donor
        fields=['Gender','Occupation','Contact_No','Email','Address','status']


class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class AdminForm(forms.ModelForm):
    class Meta:
        model=models.Admin1
        fields=['status']
        

