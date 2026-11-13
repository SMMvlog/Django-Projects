from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_name = models.CharField(max_length=200,null=True)
    mobile_no = models.CharField(max_length=10,null=False)
    city = models.CharField(max_length=100,null=True)
    age = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        db_table = "emp_table" 
