from rest_framework import viewsets
from menu.models import FoodItem
from menu_api.serializers import FoodItemSerializer

class FoodItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
