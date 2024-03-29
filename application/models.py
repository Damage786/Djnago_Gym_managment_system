from django.db import models


# Create your models here.

class Enquiry(models.Model):
    Name=models.CharField(max_length=20)
    Contact=models.CharField(max_length=20)
    Age=models.CharField(max_length=20)
    
    Email_Id=models.CharField(max_length=50)


    def __str__(self):
        return self.Name




class Member(models.Model):
    Name=models.CharField(max_length=50)
    Contact=models.CharField(max_length=20)
    Age=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    Email_Id=models.CharField(max_length=50)
    Plan=models.CharField(max_length=50)
    Join_Date=models.CharField(max_length=20)
    Expiry_Date=models.CharField(max_length=20)
    Initial_Amount=models.CharField(max_length=50)




    def __str__(self):
        return self.Name





class Equipments(models.Model):
    Name=models.CharField(max_length=20)
    Price=models.CharField(max_length=20)
    Unit=models.CharField(max_length=20)
    Date=models.CharField(max_length=20)
    Description=models.CharField(max_length=100)


    def __str__(self):
        return self.Name




class Plan(models.Model):
    Name=models.CharField(max_length=20)
    Amount=models.CharField(max_length=20)
    Duration=models.CharField(max_length=20)



    def __str__(self):
        return self.Name
    
    
class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name} {self.last_name}"
