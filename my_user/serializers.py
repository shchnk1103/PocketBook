from rest_framework import serializers

from my_user.models import MyUser


# Serializers define the API representation.

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ['url', 'username', 'email', 'first_name', 'last_name', 'about', 'password']
