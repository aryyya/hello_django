from rest_framework import viewsets
from menu.models import ItemCategory
from menu_api.serializers import ItemCategorySerializer

class ItemCategoryViewSet(viewsets.ModelViewSet):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    