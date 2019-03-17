from rest_framework import viewsets
from menu.models import MenuCategory
from menu_api.serializers import MenuCategorySerializer

class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
