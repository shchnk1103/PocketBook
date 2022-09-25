from rest_framework import viewsets, permissions

from my_user.permissions import IsOwnerOrReadOnly
from pocket_book.models import PocketBook
from pocket_book.serializers import PocketBookSerializer


# Create your views here.
class PocketBookViewSet(viewsets.ModelViewSet):
    queryset = PocketBook.objects.all().order_by('-time_of_occurrence')
    serializer_class = PocketBookSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
