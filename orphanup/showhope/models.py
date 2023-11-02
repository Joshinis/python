from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Orphans(models.Model):
    OrphanID=models.IntegerField(primary_key=True)
    Orphan_Name=models.CharField(max_length=50)
    gender_choice=(('Select the gender','Select the gender'),('Male','Male'), ('Female', 'Female'))
    Gender=models.CharField(max_length=50, choices=gender_choice,default='Select')
    DOB=models.CharField(max_length=50)
    Bgroup=models.CharField(max_length=50)
    Standard=models.CharField(max_length=50)
    Nominee=models.CharField(max_length=50)
    status=models.BooleanField(max_length=50, default=False)
    Created_date=models.DateField(auto_now_add=True)
    Updated_date=models.DateField(auto_now_add=True)


    
class Oldage(models.Model):
    OldID=models.IntegerField(primary_key=True)
    Old_Name=models.CharField(max_length=255)
    gender_choice=(('Select','Select'),('Male','Male'), ('Female', 'Female'))
    Gender=models.CharField(max_length=255, choices=gender_choice,default='Select')
    DOB=models.CharField(max_length=50)
    Age=models.CharField(max_length=10)
    Bgroup=models.CharField(max_length=50)
    Nominee=models.CharField(max_length=50)
    status=models.BooleanField(max_length=50, default=False)
    Created_date=models.DateField(auto_now_add=True)
    Updated_date=models.DateField(auto_now_add=True)

class Expence(models.Model):
    ExpenceID=models.IntegerField(primary_key=True)
    CHOICES=(('Select','Select'),('Purchases','Purchases'), ('Salary','Salary'),('Bill','Bill'),('Medicines','Medicines'),('Education','Education'),('Others','Others'))
    Type=models.CharField(max_length=255, choices=CHOICES,default='Select')
    Description=models.CharField(max_length=255)
    Amount=models.CharField(max_length=10)
    Bill_No=models.CharField(max_length=50)
    Bill_File=models.FileField(upload_to='bills/', max_length=255)
    Date=models.DateField(auto_now_add=True)
    status=models.BooleanField(max_length=50, default=False)
    Added_date=models.DateField(auto_now_add=True)
    Updated_date=models.DateField(auto_now_add=True)


class Assets(models.Model):
    Asset_ID=models.IntegerField(primary_key=True)
    CHOICES=(('Select','Select'),('Food','Food'), ('Stationary','Stationary'),('Money','Money'),('Furniture','Furniture'))
    Type=models.CharField(max_length=255, choices=CHOICES,default='Select')
    Description=models.CharField(max_length=255)
    Cost=models.CharField(max_length=10)
    Quantity=models.CharField(max_length=50)
    status=models.BooleanField(max_length=50, default=False)
    Added_date=models.DateField(auto_now_add=True)
    Updated_date=models.DateField(auto_now_add=True)

class Donor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    gender_choice=(('Select','Select'),('Male','Male'), ('Female', 'Female'))
    Gender=models.CharField(max_length=255, choices=gender_choice,default='Select')
    Occupation=models.CharField(max_length=25, null=True)
    Contact_No=models.CharField(max_length=11, null=True)
    Email=models.EmailField(max_length=254)
    Address=models.CharField(max_length=50)
    status=models.BooleanField(default=False)
    Created_date=models.DateField(auto_now_add=True)
    Updated_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name


class Admin1(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name

class Payment(models.Model):
    donorName=models.CharField(max_length=40,null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    status=models.BooleanField(default=False)



class Adoption(models.Model):
    OrphanID=models.PositiveIntegerField(null=True)
    Adopt_ID=models.IntegerField(primary_key=True)
    DonorID=models.PositiveIntegerField(null=True)    
    Adopte=models.BooleanField(max_length=20, default=False)


class Donation(models.Model):
    DonorID=models.PositiveIntegerField(null=True)
    CHOICES=(('Select','Select'),('Food','Food'), ('Stationary','Stationary'),('Money','Money'),('Furniture','Furniture'))
    Type=models.CharField(max_length=50, choices=CHOICES,default='Select')
    Amount=models.CharField(max_length=20)
    Donate_Date=models.DateField(auto_now_add=True)

class Contact(models.Model):
    ContactID=models.IntegerField(primary_key=True)
    user_Name=models.CharField(max_length=50)
    message=models.CharField(max_length=50)
    Email=models.EmailField(max_length=254)
    Created_date=models.DateField(auto_now_add=True)
    Updated_date=models.DateField(auto_now_add=True)
