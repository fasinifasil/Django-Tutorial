from django.db import models

# Create your models here.
team=(('a','marketing'),('b','HR'),('c','digital marketing'),('d','developers'))

class Employee(models.Model):
    Emp_Name    =   models.CharField(max_length=100)
    Designation =   models.CharField(max_length=100,choices=team)
    Salary      =   models.IntegerField()
    Age         =   models.IntegerField()
    Address     =   models.TextField()
    EmailId     =   models.EmailField()
    Approve     =   models.BooleanField()
    def __str__(self):
        return self.Emp_Name
class SuggestionMsg(models.Model):
    Topic   =   models.TextField()
    Emp_Name=   models.OneToOneField(Employee,on_delete=models.CASCADE)
    def __str__(self):
        return self.Topic

class LeaveReport(models.Model):
    Leave_Date  =   models.DateField()
    Reason      =   models.CharField(max_length=100)
    Emp_Name=   models.ForeignKey(Employee,on_delete=models.CASCADE)

    def __str__(self):
        return self.Reason


class EmployeeData(models.Model):
    Emply_Name    =   models.CharField(max_length=100)
    Designation =   models.CharField(max_length=100,choices=team)
    Salary      =   models.IntegerField()
    def __str__(self):
        return self.Emply_Name


class AccountDetails(models.Model):
    AccountData   =   models.TextField()
    Emply_Name=   models.OneToOneField(Employee,on_delete=models.CASCADE)
    def __str__(self):
        return self.AccountData
