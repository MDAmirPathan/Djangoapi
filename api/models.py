from django.db import models

# Create your models here.


#create company model
class Company(models.Model):

    TYPES = (('IT','IT'),
             ('Non IT', 'Non IT'),
             ('Mobile No', 'Mobile No'))

    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    types=models.CharField(max_length=100, choices=TYPES)
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name+'--'+self.location


# employee Model
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    address = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50, choices=(
        ('Manager', 'Manager'),
        ('Software Developer','sd'),
        ('Projrct Manager','pm')
        ))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name+'--'+self.company.name
