from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework import status
from rest_framework.response import Response
from refni_io.serializers.UserRegister import UserRegisterSerializer


class UserRegisterView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny, )

    def post(self, request, _format=None):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'OK'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
