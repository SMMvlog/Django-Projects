from rest_framework.views import APIView
from api.models import Employee
from api.serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status

class EmployeeCrudOperation(APIView):
    def post(self,request):
        try:
            request_data = request.data
            action_type = request_data.get("action_type")
            emp_code = request_data.get("emp_code")
            first_name = request_data.get("first_name")
            middle_name = request_data.get("middle_name")
            last_name = request_data.get("last_name")
            designation = request_data.get("designation")
            is_active = request_data.get("is_active")
            mobile_number = request_data.get("mobile_number")
            manager_id = request_data.get("manager_id")

            if action_type == "add_employee":
                is_created = EmployeeSerializer.insert(self,request_data)
                print("is_created---",is_created)
                if is_created:
                    return Response(data = {"Msg":"Employee added successfully"},status = status.HTTP_200_OK)
            elif action_type == "update_employee":
                if emp_code:
                    is_updated = EmployeeSerializer.update(self,request_data)
                    print("is_updated---",is_updated)
                    if is_updated:
                        return Response(data = {"Msg":"Employee added successfully"},status = status.HTTP_200_OK)
                else:
                    return Response(data={"Msg":"emp_code not given"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print("ex---views-----",ex)
            return ex
             
        