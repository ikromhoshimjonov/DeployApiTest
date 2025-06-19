from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from apps.models import Categories, Product
from apps.serializers import CategoryModelSerializer, ProductModelSerializer

@extend_schema(tags=["category"])
class CategoryViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoryModelSerializer
    
@extend_schema(tags=["product"])
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

