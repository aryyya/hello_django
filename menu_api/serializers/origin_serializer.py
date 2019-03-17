from rest_framework import serializers
from menu.models import Origin

class OriginSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Origin
        fields = (
            'url',
            'city',
            'state',
            'country',
            'latitude',
            'longitude',
            'grower_name',
            'grower_notes',
            'tea_items'
        )
