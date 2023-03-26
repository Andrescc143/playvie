from django.contrib.auth.models import User, Group
from rest_framework import serializers

#The serializer are related through the HyperlinkedModel, which adds URL to access the related data from the other table/entity

#To represent the data related to each user
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

#To represent the data from each Group of users
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']