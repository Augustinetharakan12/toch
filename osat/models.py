import datetime
from django.db import models

class alumni(models.Model):
    fname=models.CharField(max_length=200,null=True)
    lname=models.CharField(max_length=200,null=True)
    year_pass=models.IntegerField(null=True)
    id = models.IntegerField(primary_key=True)
    student=models.CharField(max_length=2,null=True)#y or N
    inst_name=models.CharField(max_length=200,null=True)
    phno=models.CharField(max_length=15,null=True)
    email=models.CharField(max_length=100,null=True)
    #dob=models.DateField
    # address info
    a_street = models.CharField(max_length=200,null=True)
    a_city = models.CharField(max_length=200,null=True)
    a_state = models.CharField(max_length=200,null=True)
    a_country = models.CharField(max_length=200,null=True)
    a_pin = models.CharField(max_length=50,null=True)
    def disp(self):
        print("name=",self.fname, end="\t")
        print("last name=",self.lname, end="\t")
        print("year of pass=",self.year_pass,end="\t")
        print("phone no=",self.phno,end="\t")
    def __str__(self):
        return self.fname+' '+ self.lname
class notif(models.Model):
    fname=models.CharField(max_length=50,null=True)
    title=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=50,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title+' '+ self.fname

class ec(models.Model):
    fname=models.CharField(max_length=50,null=True)
    lname=models.CharField(max_length=50,null=True)
    def __str__(self):
        return ' '+ self.fname
class det(models.Model):
    h=models.CharField(max_length=50,null=True)




