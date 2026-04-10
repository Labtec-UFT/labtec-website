from django.urls import path
from app.interfaces.public.api.v1.users.views import (
    UserListCreateView,
    UserDetailView,
    MeView,
    CreateStaffUserView,
)

urlpatterns = [
    path("", UserListCreateView.as_view(), name="users-list-create"),
    path("<int:pk>/", UserDetailView.as_view(), name="users-detail"),
    path("me/", MeView.as_view(), name="users-me"),
    path("staff/", CreateStaffUserView.as_view(), name="users-create-staff"),
]