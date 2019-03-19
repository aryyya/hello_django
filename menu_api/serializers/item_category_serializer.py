from menu.models import ItemCategory
from rest_framework import serializers

class ItemCategorySerializer(serializers.HyperlinkedModelSerializer):

    menu_category = serializers.HyperlinkedRelatedField(view_name='menucategory-detail', read_only=True)

    tea_items = serializers.HyperlinkedRelatedField(source='teaitem_set', view_name='teaitem-detail', read_only=True, many=True)

    food_items = serializers.HyperlinkedRelatedField(source='fooditem_set', view_name='fooditem-detail', read_only=True, many=True)

    class Meta:
        model = ItemCategory
        fields = (
            'url',
            'name',
            'menu_category',
            'short_description',
            'long_description',
            'tea_items',
            'food_items'
        )
