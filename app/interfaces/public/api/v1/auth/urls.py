from django.urls import path, include

from app.interfaces.public.api.v1.auth.auth_views import (
    CookieTokenObtainPairView,
    CookieTokenRefreshView,
    MeView,
    LogoutView
)

urlpatterns = [
    path('token/', CookieTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', CookieTokenRefreshView.as_view(), name='token-refresh'),
    path('me/', MeView.as_view(), name='me'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
