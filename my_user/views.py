from rest_framework import viewsets, permissions

from my_user.models import MyUser
from my_user.permissions import IsOwnerOrReadOnly
from my_user.serializers import UserSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all().order_by('-start_date')
    serializer_class = UserSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
