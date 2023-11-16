from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    email=models.EmailField(unique=True)
    contact=models.CharField(max_length=10,null=True)
    department=models.CharField(max_length=100)
    salary=models.PositiveIntegerField()
    profile_pic=models.ImageField(upload_to="images",null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    
    def __str__(self):
        return self.name
        
    
