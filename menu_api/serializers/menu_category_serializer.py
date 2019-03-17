from rest_framework import serializers
from menu.models import MenuCategory

class MenuCategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MenuCategory
        fields = (
            'url',
            'name',
            'itemcategory_set'
        )
