from django.contrib.auth.hashers import make_password
from rest_framework import viewsets, permissions, filters

from my_user.models import MyUser
from my_user.permissions import IsOwnerOrReadOnly
from my_user.serializers import UserSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = MyUser.objects.all().order_by('-start_date')
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['email', 'username']

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset

        if not user.pk:
            return queryset.none()
        else:
            if user.is_superuser:
                return queryset

            return queryset.filter(username=user)
