from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.contrib import admin
from django.urls import path
from menu.models import Origin, TeaItem
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class OriginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Origin
        fields = ('city', 'state', 'country', 'latitude', 'longitude', 'grower_name', 'grower_notes')

class TeaItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeaItem
        fields = ('origin', 'tasting_notes', 'year', 'leaves', 'price_bar', 'price_bowl', 'price_shot', 'price_retail')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OriginViewSet(viewsets.ModelViewSet):
    queryset = Origin.objects.all()
    serializer_class = OriginSerializer

class TeaItemViewSet(viewsets.ModelViewSet):
    queryset = TeaItem.objects.all()
    serializer_class = TeaItemSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'origins', OriginViewSet)
router.register(r'tea-items', TeaItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
