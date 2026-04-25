from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from app.domains.users.views import CustomTokenObtainView, MeView

urlpatterns = [
    path('admin', admin.site.urls),
    path('token', CustomTokenObtainView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
    path('me/', MeView.as_view()),
]
