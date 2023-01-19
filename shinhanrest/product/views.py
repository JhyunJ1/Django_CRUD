from rest_framework import generics, mixins
from .models import Product
from .serializers import ProductSerializer

class ProductListView(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return Product.objects.all().order_by('id')
    

    def get(self, request, *args, **kwargs):
        # Queryset
        # Serialize
        # return Response
        return self.list(request, args, kwargs)