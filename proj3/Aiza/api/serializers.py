from rest_framework import serializers
from api.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    def insert(self,request):
        try:
            first_name = request.get("first_name")
            middle_name = request.get("middle_name")
            last_name = request.get("last_name")
            designation = request.get("designation")
            is_active = request.get("is_active")
            mobile_number = request.get("mobile_number")
            salary = request.get("salary")
            manager_id = request.get("manager_id")

            insert_dict = {}

            if first_name:
                insert_dict["first_name"] = first_name
            if middle_name:
                insert_dict["middle_name"] = middle_name
            if last_name:
                insert_dict["last_name"] = last_name
            if designation:
                insert_dict["designation"] = designation
            if mobile_number:
                insert_dict["mobile_number"] = mobile_number
            if salary:
                insert_dict["salary"] = salary
            if manager_id:
                manager = Employee.objects.get(id=manager_id)
                insert_dict["manager_id"] = manager

            if insert_dict:
                obj_created = Employee.objects.create(**insert_dict)
                print("obj_created-------",obj_created)
                return obj_created
            else:
                return False
        except Exception as ex:
            print("ex----serializer---",ex)
            return ex
        
    def update(self,request):
        try:
            first_name = request.get("first_name")
            middle_name = request.get("middle_name")
            last_name = request.get("last_name")
            designation = request.get("designation")
            is_active = request.get("is_active")
            mobile_number = request.get("mobile_number")
            salary = request.get("salary")
            manager_id = request.get("manager_id")
            emp_code = request.get("emp_code")

            emp_obj =Employee.objects.get(emp_code=emp_code)
            if emp_obj:
                if first_name:
                    emp_obj.emp_obj = first_name
                if middle_name:
                    emp_obj.middle_name = middle_name
                if last_name:
                    emp_obj.last_name = last_name
                if designation:
                    emp_obj.designation = designation
                if mobile_number:
                    emp_obj.mobile_number = mobile_number
                if salary:
                    emp_obj.salary = salary
                if emp_obj:
                    if is_active == "in_active":
                        emp_obj.is_active = False
                    elif is_active == "active":
                        emp_obj.is_active = True
                emp_obj.save()
            else:
                return False
        except Exception as ex:
            print("ex----serializer---",ex)
            return ex