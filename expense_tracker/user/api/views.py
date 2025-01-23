from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import UserSerializer, LoginSerializer


class CreateUserView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": status.HTTP_200_OK,
                    "data": serializer.data,
                }
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUserView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(
                {
                    "status": status.HTTP_200_OK,
                    "message": "User logged in successfully",
                    "data": data,
                }
            )
        else:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
