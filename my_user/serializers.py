from rest_framework import serializers

from my_user.models import MyUser


# Serializers define the API representation.

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ['url', 'pk', 'username', 'account_img', 'email', 'first_name', 'last_name', 'about', 'password',
                  'is_superuser']
