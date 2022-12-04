from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions

from tutorial.quickstart.serializers import UserSerializer, GroupSerializer

"""
TODO:
	- ? Rather than write multiple views we're grouping together all the common behavior
	into classes called ViewSets.
	- ? We can easily break these down into individual views if we need to, but using
	viewsets keeps the view logic nicely organized as well as being very concise.
"""


class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint for users reading or mutation
	TODO:
		- Abstract/Encapslute query and serializer class knowledge to another layer.
		- Reasons
			- SoCs
			- SRP - SOLID
			- Testability
			- Maintainability
			- Reuse
			- Boilerplate code
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint for groups reading or mutation
	TODO:
		- Abstract/Encapslute query and serializer class knowledge to another layer.
		- Reasons
			- SoCs
			- SRP - SOLID
			- Testability
			- Maintainability
			- Reuse
			- Boilerplate code
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
	permission_classes = [permissions.IsAuthenticated]

