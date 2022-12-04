from django.contrib.auth.models import User, Group
from rest_framework import serializers

# TODO: Refactor folder structure to: serializers/user.py and serializers/group.py

"""
TODO:
	- ? Serializers
	- ? Why `HyperlinkedModelSerializer`s are more RESTful than pks and fks
	- ? Meta class
"""

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
			model = Group
			fields = ['url', 'name']
