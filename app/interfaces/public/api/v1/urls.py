from django.urls import path, include

from app.interfaces.public.api.v1 import management_urls, public_urls

urlpatterns = [
    path('auth/', include('app.interfaces.public.api.v1.auth.urls')),
    path('public/', include(public_urls)),
    path('management/', include(management_urls)),
]