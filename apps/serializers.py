from rest_framework.serializers import ModelSerializer

from apps.models import Categories, Product


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = "name",

class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "name","price"