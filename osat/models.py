from django.db import models

class alumni(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    year_pass=models.IntegerField(max_length=5)
    id = models.IntegerField(primary_key=True)
    student=models.CharField(max_length=2)#y or N
    inst_name=models.CharField(max_length=200,null=True)
    phno=models.CharField(max_length=15)
    email=models.CharField(max_length=100)
    #dob=models.DateField
    # address info
    a_street = models.CharField(max_length=200,null=True)
    a_city = models.CharField(max_length=200,null=True)
    a_state = models.CharField(max_length=200,null=True)
    a_country = models.CharField(max_length=200,null=True)
    a_pin = models.CharField(max_length=50)
    def __str__(self):
        return self.fname+' '+ self.lname



