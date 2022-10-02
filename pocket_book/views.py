from rest_framework import viewsets

from pocket_book.models import PocketBook
from pocket_book.permissions import IsOwner
from pocket_book.serializers import PocketBookSerializer


# Create your views here.
class PocketBookViewSet(viewsets.ModelViewSet):
    queryset = PocketBook.objects.all().order_by('-time_of_occurrence')
    serializer_class = PocketBookSerializer

    permission_classes = [IsOwner]

    def get_queryset(self):
        if not self.request.user.pk:
            queryset = []
            return queryset
        else:
            queryset = self.queryset

            if self.request.user.is_superuser:
                return queryset
            return queryset.filter(author=self.request.user)
