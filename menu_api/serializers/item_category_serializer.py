from rest_framework import serializers
from menu.models import ItemCategory

class ItemCategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ItemCategory
        fields = (
            'url',
            'name',
            'menu_category',
            'short_description',
            'long_description',
            'teaitem_set',
            'fooditem_set'
        )
