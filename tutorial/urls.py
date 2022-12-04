from django.urls import include, path
from rest_framework import routers

from tutorial.quickstart import views


# Automatic URL routing configuration. This is posible due to ViewSet usage.
router = routers.DefaultRouter()
router.register(prefix=r'users', viewset=views.UserViewSet)
router.register(prefix=r'groups', viewset=views.GroupViewSet)

urlpatterns = [
	path(route='', view=include(router.urls)),
	# default login and logout for browsable API usage.
	path(route='', view=include('rest_framework.urls'), name='rest_framework'),
]
