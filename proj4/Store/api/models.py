from django.db import models

class UserMaster(models.Model):
    user_name = models.CharField(max_length=50,null=False)
    mobile_number = models.CharField(max_length=12,null=False)
    address = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        db_table = "user_master"