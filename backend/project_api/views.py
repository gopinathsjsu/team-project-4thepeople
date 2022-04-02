from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# API View here
class CustomersAPI(APIView):
    def get(self, request):
        return Response(
            {"status": "success",
             "data": "Successful Get Request"
            }, status=status.HTTP_200_OK)
