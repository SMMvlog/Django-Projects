from rest_framework.views import APIView
from api.models import Employee
from rest_framework.response import Response
from rest_framework import status
class EmployeeView(APIView):
    def post(self,request):
        try:
            request_data = request.data
            emp_name = request_data.get("emp_name")
            mobile_number = request_data.get("mobile_number")
            city = request_data.get("city")
            age = request_data.get("age")
            object_created = Employee.objects.create(emp_name=emp_name,mobile_no=mobile_number,city=city,age=age)
            if object_created:
                return Response(data={"Message":"Data Inserted Successfully"},status=status.HTTP_200_OK)
            return Response(data={"Message":"Something went wrong"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print("exxxx--",ex)
            return Response(data={"Message":"Internal Server error"},status=status.HTTP_400_BAD_REQUEST)
