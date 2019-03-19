from rest_framework import serializers
from menu.models import Origin

class OriginSerializer(serializers.HyperlinkedModelSerializer):

    tea_items = serializers.HyperlinkedRelatedField(source='teaitem_set', view_name='teaitem-detail', read_only=True, many=True)

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
