from rest_framework import viewsets, permissions

from pocket_book.models import PocketBook
from pocket_book.permissions import IsOwner
from pocket_book.serializers import PocketBookSerializer


# Create your views here.
class PocketBookViewSet(viewsets.ModelViewSet):
    queryset = PocketBook.objects.all().order_by('-time_of_occurrence')
    serializer_class = PocketBookSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwner]
