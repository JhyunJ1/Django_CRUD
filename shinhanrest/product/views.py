from rest_framework import generics, mixins
from .models import Product
from .serializers import ProductSerializer

class ProductListView(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView,
    ):

    serializer_class = ProductSerializer

    def get_queryset(self):
        product = Product.filter.all()
        name = request.query_params.get('name')
        if name:
            product = product.filter(name__contains=name)
        
        return product.order_by('id')
        

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)