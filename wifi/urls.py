from django.conf.urls import patterns, include, url
from rest_framework import routers, serializers, viewsets
from api.serializers import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'^resources/WifiUsers', UserViewSet)
router.register(r'^resources/statistics_hits', ShowsViewSet )
router.register(r'^resources/rek_company', AdvertisingCampaignViewSet)
router.register(r'^resources/auth', AuthViewSet, 'WifiUsers')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wifi.views.home', name='home'),
    # url(r'^wifi/', include('wifi.foo.urls')),
    url(r'^', include(router.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api_web/', include('rest_framework.urls', namespace='rest_framework')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
