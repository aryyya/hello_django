from rest_framework.routers import DefaultRouter
from . import views
from django.urls import include, path

router = DefaultRouter()
router.register(r'origins', views.OriginViewSet)
router.register(r'tea-items', views.TeaItemViewSet)
router.register(r'food-items', views.FoodItemViewSet)
router.register(r'item-categories', views.ItemCategoryViewSet)
router.register(r'menu-categories', views.MenuCategoryViewSet)

urlpatterns = [
    path(r'', include(router.urls))
]
