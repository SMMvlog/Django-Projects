from django.db import models
import random
import string
# Create your models here.


def generate_emp_code():
    letters = random.choices(string.ascii_letters, k=3)
    digits = random.choices(string.digits, k=5)
    emp_code = ''.join(letters + digits)
    return emp_code

class Employee(models.Model):
    emp_code = models.CharField(max_length=200,null=False)
    first_name = models.CharField(max_length=200,null=False)
    middle_name = models.CharField(max_length=200,null=True,default=None)
    last_name = models.CharField(max_length=200,null=False)
    salary = models.IntegerField(null=True)
    designation = models.CharField(max_length=200,null=False)
    is_active = models.BooleanField(default=True)
    mobile_number = models.CharField(max_length=12,null=False)
    manager_id = models.ForeignKey('self',related_name="manager_post",
        null=True,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def save(self, *args, **kwargs):
        if not self.emp_code:
            # Ensure uniqueness before saving
            while True:
                emp_code = generate_emp_code()
                if not Employee.objects.filter(emp_code=emp_code).exists():
                    self.emp_code = emp_code
                    break
        super().save(*args, **kwargs)
    class Meta:
        db_table = 'employee_master'