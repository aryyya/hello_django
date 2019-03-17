from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path
from menu_api import views
from menu.models import Origin, TeaItem, FoodItem, ItemCategory, MenuCategory
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'origins', views.OriginViewSet)
router.register(r'tea-items', views.TeaItemViewSet)
router.register(r'food-items', views.FoodItemViewSet)
router.register(r'item-categories', views.ItemCategoryViewSet)
router.register(r'menu-categories', views.MenuCategoryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
