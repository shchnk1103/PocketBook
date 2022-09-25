from rest_framework import serializers

from pocket_book.models import PocketBook


class PocketBookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PocketBook
        fields = [
            'url', 'id', 'author', 'image', 'title', 'amount', 'created_date', 'time_of_occurrence'
        ]
