from django.urls import path

from app.interfaces.public.api.v1.users.views import CreateUserView, CreateStaffUserView

urlpatterns = [
    path('create/staff/', CreateStaffUserView.as_view(), name='create-staff'),
    path('create/', CreateUserView.as_view(), name='create-users'),
]