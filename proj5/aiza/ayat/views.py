from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Home(APIView):
    def post(self,req):
        req_data = req.data
        name = req_data.get("name")
        if name:
            return Response(data={"message":f"name is {name}"},status =status.HTTP_200_OK )
        return Response(data={"message":"Please provide your name"},status =status.HTTP_412_PRECONDITIN_FAILED)
        
        