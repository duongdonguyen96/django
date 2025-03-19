from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from .selectors import UserSelector
from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema(tags=["Users"])
class UserListView(generics.ListCreateAPIView):
    queryset = UserSelector.get_all_users()
    serializer_class = UserSerializer


@extend_schema_view(
    get=extend_schema(summary="get user by id"),
    put=extend_schema(summary="update user"),
    delete=extend_schema(summary="delete user"),
)
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
