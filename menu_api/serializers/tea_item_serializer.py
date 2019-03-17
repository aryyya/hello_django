from rest_framework import serializers
from menu.models import TeaItem

class TeaItemSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = TeaItem
        fields = (
            'url',
            'name',
            'category',
            'stock',
            'translation',
            'punchline',
            'bartender_notes',
            'origin',
            'tasting_notes',
            'year',
            'leaves',
            'price_bar',
            'price_bowl',
            'price_shot',
            'price_retail'
        )
