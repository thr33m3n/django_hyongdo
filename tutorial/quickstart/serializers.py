from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Restaurant


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    images = serializers.ImageField(use_url=True)
    class Meta:
        model = Restaurant
        fields = ('id_no', 'subway_line', 'station', 'category',
        'name', 'address', 'phone', 'workingtime', 'likes',
        'explanation', 'images')
