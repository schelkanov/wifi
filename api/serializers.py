# -- coding: utf-8 --
from django.conf import settings
from django.contrib.auth.models import User,  Group, Permission
from django.db.models.signals import post_save
from api.models import *
from rest_framework import routers, serializers, viewsets
from rest_framework.permissions import *
from rest_framework.response import Response
from django.dispatch import receiver
import hashlib
from rest_framework import generics
from rest_framework.mixins import * 
from rest_framework.views import *
from django.db.models import Q
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token



'''For Users'''
class WifiUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = WifiUsers
        fields = ('id', 'username' ,'first_name', 'password', 'last_name', 'role','address', 'companyName', 'phone', 'email' ,'additional', 'groups', 'is_superuser', 'is_active', )        
        authentication_classes = (IsAuthenticated)
        
    def create(self, validated_data):
        validated_data['password'] = User.set_password(validated_data['password'])
        return  WifiUsers.objects.create(**validated_data)
    def has_permission(self, request, view, obj=None):
    # Write permissions are only allowed to the owner of the snippet
        return obj is None or obj.from_user == request.user

class UserViewSet(viewsets.ModelViewSet, UpdateModelMixin, DestroyModelMixin):
    queryset = WifiUsers.objects.all()
    serializer_class = WifiUsersSerializer

'''Info advertising company'''
class AdvertisingCampaignSerializer(serializers.ModelSerializer, UpdateModelMixin, DestroyModelMixin):
    class Meta:
        model = AdvertisingCampaign
#        fields = ('user', 'name_compaign', 'banner', 'desc_compaign', 'count_shows', 'shows_peer_user', 'shows_interval')

class AdvertisingCampaignViewSet(viewsets.ModelViewSet, UpdateModelMixin, DestroyModelMixin):
    queryset = AdvertisingCampaign.objects.all()
    serializer_class = AdvertisingCampaignSerializer

'''Info about hits in advertising company'''
class WifiShowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WifiShows

class ShowsViewSet(viewsets.ModelViewSet):
   queryset = WifiShows.objects.all()
   serializer_class = WifiShowsSerializer

'''Auth users'''
class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = WifiUsers

class AuthViewSet(APIView):
    """
    Authentication is needed for this methods
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
 
    def get(self, request, format=None):
        return Response({'detail': "I suppose you are authenticated"})
