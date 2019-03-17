from menu_api.serializers import OriginSerializer
from menu.models import Origin
from rest_framework import viewsets

class OriginViewSet(viewsets.ModelViewSet):
    queryset = Origin.objects.all()
    serializer_class = OriginSerializer
