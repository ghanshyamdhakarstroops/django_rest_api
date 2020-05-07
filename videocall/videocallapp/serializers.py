from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Hero

class HeroSerialize(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Hero
		fields = ['url','owner', 'name', 'alise']

class UserSerializer(serializers.HyperlinkedModelSerializer):
	snippets = serializers.HyperlinkedRelatedField(many=True, view_name='hero-detail', read_only=True)
	class Meta:
		model = User
		fields = ['url', 'id', 'username', 'snippets']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']