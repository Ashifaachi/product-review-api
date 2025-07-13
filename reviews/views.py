from rest_framework import viewsets, permissions, status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import generics
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .models import Product, Review
from .serializers import (
    ProductSerializer,
    ReviewSerializer,
    UserRegisterSerializer
)
from .permissions import IsAdminOrReadOnly, IsAuthenticatedAndNotAdmin

# --------------------------
# Product ViewSet
# --------------------------
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]

# --------------------------
# Review ViewSet (Nested)
# --------------------------
class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedAndNotAdmin]

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def perform_create(self, serializer):
        product_id = self.kwargs['product_pk']
        user = self.request.user
        if Review.objects.filter(product_id=product_id, user=user).exists():
            raise serializers.ValidationError("You already reviewed this product.")
        serializer.save(user=user, product_id=product_id)

# --------------------------
# Register API
# --------------------------
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --------------------------
# Login API
# --------------------------
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# --------------------------
# Logout API
# --------------------------
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)

# --------------------------
# Admin-Only: User List
# --------------------------
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [IsAdminUser]
