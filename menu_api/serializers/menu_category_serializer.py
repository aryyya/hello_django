from rest_framework import serializers
from menu.models import MenuCategory

class MenuCategorySerializer(serializers.HyperlinkedModelSerializer):

    item_categories = serializers.HyperlinkedRelatedField(source='itemcategory_set', view_name='itemcategory-detail', read_only=True, many=True)

    class Meta:
        model = MenuCategory
        fields = (
            'url',
            'name',
            'item_categories'
        )
