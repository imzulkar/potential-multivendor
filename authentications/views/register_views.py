from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from authentications.models import User
from authentications.serializers import NewUserSerializer

class UserRegistrationView(ModelViewSet):
    """
    User Registration View
    """
    serializer_class = NewUserSerializer
    queryset = User.objects.all()
    http_method_names = ["post"]
    permission_classes = []

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User Registered Successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)