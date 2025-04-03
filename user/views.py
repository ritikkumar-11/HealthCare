from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView): # used CreateAPIview beacuse it only allow the POST, so exposed api end point like list or delete
    """
    API endpoint for user registration.
    """
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully."},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Token Obtain View (Login)
class LoginView(TokenObtainPairView):
    pass

# Token Refresh View (for renewing JWT)
class RefreshTokenView(TokenRefreshView):
    pass

