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
        

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)