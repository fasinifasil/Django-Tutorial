from django.db import models

# Create your models here.
team    =   (('a','marketing'),('b','graphic designer'),('c','Developer'),('d','degital marketing'),('e','admin'))
class Employee(models.Model):
    Emp_Name    =   models.CharField(max_length=100)
    Emp_Team    =   models.CharField(max_length=100,choices=team)
    Salary      =   models.IntegerField()
    Age         =   models.IntegerField()
    Address     =   models.TextField()
    Email       =   models.EmailField()
    approve  =   models.BooleanField(default=False)

    def __str__(self):
        return self.Emp_Name
