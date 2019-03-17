from rest_framework import viewsets
from menu.models import TeaItem
from menu_api.serializers import TeaItemSerializer

class TeaItemViewSet(viewsets.ModelViewSet):
    queryset = TeaItem.objects.all()
    serializer_class = TeaItemSerializer
