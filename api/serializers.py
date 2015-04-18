# -- coding: utf-8 --
from api.models import *
from rest_framework import routers, serializers, viewsets
import hashlib
'''For Users'''
class WifiUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = WifiUsers
        fields = ('id','first_name', 'last_name', 'company_name', 'phone', 'email', 'password' ,'info', )        
    def create(self, validated_data):
        validated_data['password'] = hashlib.md5( validated_data['password'] ).hexdigest()
        return WifiUsers(**validated_data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = WifiUsers.objects.all()
    serializer_class = WifiUsersSerializer

'''Info advertising company'''
class AdvertisingCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisingCampaign
        fields = ('user', 'name_compaign', 'banner', 'desc_compaign', 'count_shows', 'shows_peer_user', 'shows_interval')

class AdvertisingCampaignViewSet(viewsets.ModelViewSet):
    queryset = AdvertisingCampaign.objects.all()
    serializer_class = AdvertisingCampaignSerializer
'''Info about hits in advertising company'''
class WifiShowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WifiShows

class ShowsViewSet(viewsets.ModelViewSet):
   queryset = WifiShows.objects.all()
   serializer_class = WifiShowsSerializer
