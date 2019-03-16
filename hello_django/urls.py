from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.contrib import admin
from django.urls import path
from menu.models import Origin, TeaItem, FoodItem, ItemCategory, MenuCategory
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class OriginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Origin
        fields = ('url', 'city', 'state', 'country', 'latitude', 'longitude', 'grower_name', 'grower_notes', 'teaitem_set')

class TeaItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeaItem
        fields = ('url', 'name', 'category', 'stock', 'translation', 'punchline', 'bartender_notes', 'origin', 'tasting_notes', 'year', 'leaves', 'price_bar', 'price_bowl', 'price_shot', 'price_retail')

class FoodItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeaItem
        fields = ('url', 'name', 'category', 'stock', 'translation', 'punchline', 'bartender_notes')

class ItemCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ItemCategory
        fields = ('url', 'name', 'menu_category', 'short_description', 'long_description', 'teaitem_set', 'fooditem_set')

class MenuCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ('url', 'name', 'itemcategory_set')

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

class FoodItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class ItemCategoryViewSet(viewsets.ModelViewSet):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer

class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'origins', OriginViewSet)
router.register(r'tea-items', TeaItemViewSet)
router.register(r'food-items', FoodItemViewSet)
router.register(r'item-categories', ItemCategoryViewSet)
router.register(r'menu-categories', MenuCategoryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
