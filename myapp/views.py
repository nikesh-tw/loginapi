from django.http import JsonResponse
from .serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


# #Register Api
class RegisterApi(APIView):

    def post(self,request):
        try:

            #serializer = self.get_serializer(data = request.data)
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"User Created Successfully , Now perform Login to get your token"})
            else:
                return JsonResponse(serializer.errors)

        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)