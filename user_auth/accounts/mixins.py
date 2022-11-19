from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from accounts.serializer import UserSerializer


class BaseUserViewMixin:
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = User.objects.all().order_by("id")
