from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, serializers, status
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from app.domains.users.serializer import UserSerializer
from app.interfaces.public.api.permissions import IsSelfOrAdmin
User = get_user_model()


class CreateStaffUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, min_length=8)

class CreateStaffUserView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = CreateStaffUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        if User.objects.filter(email=email).exists():
            raise ValidationError({"email": ["Usuario ja existe."]})

        user = User.objects.create_user(
            email=email,
            password=password
        )

        user.is_staff = True
        user.save()

        return Response(
            {
                "email": user.email,
                "is_staff": user.is_staff,
            },
            status=status.HTTP_201_CREATED,
        )

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]
        return [IsAdminUser()]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == "DELETE":
            return [IsAdminUser()]
        return [IsAuthenticated(), IsSelfOrAdmin()]

    def check_object_permissions(self, request, obj):
        super().check_object_permissions(request, obj)
        if request.method in ["PUT", "PATCH"] and not (request.user.is_staff or obj.pk == request.user.pk):
            raise PermissionDenied("Voce nao tem permissao para editar este usuario.")

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)