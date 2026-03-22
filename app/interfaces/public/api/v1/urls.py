from django.urls import path, include

urlpatterns = [
    path('auth/', include('app.interfaces.public.api.v1.auth.urls')),
    path('users/', include('app.interfaces.public.api.v1.users.urls')),
    path('news/', include('app.interfaces.public.api.v1.news.urls')),
]