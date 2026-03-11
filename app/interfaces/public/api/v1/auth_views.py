from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework import serializers, status
from decouple import config

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'is_staff']


class CookieTokenObtainPairView(TokenObtainPairView):
    """
    Login: retorna o access token no body e seta o refresh token
    como httpOnly cookie — o cliente JS nunca consegue ler o refresh token.
    """
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            refresh_token = response.data.pop('refresh')
            response.set_cookie(
                key='refresh_token',
                value=refresh_token,
                httponly=True,
                secure= config('PRODUCTION'),  # True em produção (HTTPS)
                samesite='Lax',
                max_age=60 * 60 * 24 * 7,
                path='/',
            )

        return response


class CookieTokenRefreshView(TokenRefreshView):
    """
    Renova o access token lendo o refresh token do httpOnly cookie.
    """
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get('refresh_token')

        if not refresh_token:
            return Response(
                {"detail": "Refresh token não encontrado."},
                status=401
            )

        data = request.data.copy()
        data['refresh'] = refresh_token

        request._full_data = data

        return super().post(request, *args, **kwargs)


class MeView(APIView):
    """
    Retorna os dados do usuário autenticado.
    Requer access token válido no header Authorization.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class LogoutView(APIView):
    """
    Logout: invalida o refresh token no servidor e apaga o cookie.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')

        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
            except TokenError:
                pass

        response = Response({'detail': 'Logout realizado com sucesso.'})
        response.delete_cookie('refresh_token', path='/')
        return response
