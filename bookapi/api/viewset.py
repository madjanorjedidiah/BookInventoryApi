from rest_framework import viewsets
from .models import *
from .serializers import *
from django.core.exceptions import PermissionDenied
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import status, filters
from django.contrib.auth.models import User
from . import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken




class InventoryView(viewsets.ViewSet):
	# queryset = Inventory.objects.all()
	serializer_class =  InventorySerializer
	

	def list(self, request):
		if not request.user.has_perm('api.view_inventory'):
			raise PermissionDenied()
		else:
			queryset = Inventory.objects.all()
			serializer_class = InventorySerializer(queryset, many=True)
			return Response(serializer_class.data)


	def perform_create(self, serializer):
		serializer.save()

	def create(self, request):
		if not request.user.has_perm('api.add_inventory'):
			raise PermissionDenied()
		else:
			serializd = InventorySerializer(data=request.data)

			if serializd.is_valid():
				self.perform_create(serializd)
				return Response(serializd.data)
			else:
				return Response({
	                'status': 'Bad request'
	            }, status=status.HTTP_404_NOT_FOUND)



	@action(detail=False)
	def get_list(self, request):
		queryset = Inventory.objects.all()
		serializer_class = InventorySerializer(queryset, many=True)
		return Response(serializer_class.data)

	

	def retrieve(self, request, pk=None):
		queryset = Inventory.objects.all()
		obj = get_object_or_404(queryset, pk=pk)
		serializer_class = InventorySerializer(obj)
		return Response(serializer_class.data)



	def update(self, request, pk=None):
		##   updates an object

		try:
			obj = Inventory.objects.get(pk=pk)
		except SC.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		if not request.user.has_perm('api.change_inventory'):
			raise PermissionDenied()
		else:
			serializer = InventorySerializer(obj, data=request.data)
			if serializer.is_valid():
				self.perform_create(serializd)
				return Response(serializd.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def partial_update(self, request, pk=None):
		##  update part of an object
		try:
			obj = Inventory.objects.get(pk=pk)
		except SC.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		if not request.user.has_perm('api.change_inventory'):
			raise PermissionDenied()
		else:
			serializer = InventorySerializer(obj, data=request.data)
			if serializer.is_valid():
				self.perform_create(serializd)
				return Response(serializd.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def destroy(self, request, pk=None):
		##  deletes an object
		try:
			obj = Inventory.objects.get(pk=pk)
		except SC.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		if not request.user.has_perm('api.delete_inventory'):
			raise PermissionDenied()
		else:
			return Response({'method':'delete'})



class UserProfileViewSet(viewsets.ModelViewSet):
	''' handles create, update and read'''

	authentication_classes = (TokenAuthentication,)
	permission_classes = (permissions.UpdateOwnProfile,)
	serializer_class = UserSerializer
	queryset = User.objects.all()
	filter_backends = (filters.SearchFilter,)
	search_fields = ('username', 'email',)


class LoginViewSet(viewsets.ViewSet):

	serializer_class = AuthTokenSerializer

	def create(self, request):
		return ObtainAuthToken().as_view()(request=request._request)