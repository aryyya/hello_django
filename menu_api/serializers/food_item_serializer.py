from rest_framework import serializers
from menu.models import FoodItem

class FoodItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FoodItem
        fields = (
            'url',
            'name',
            'category',
            'stock',
            'translation',
            'punchline',
            'bartender_notes'
        )
