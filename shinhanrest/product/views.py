from rest_framework import generics, mixins
from .models import Product, Comment
from .serializers import ProductSerializer, CommentSerializer
from .paginations import ProductLargePagination

class CommentListView(
        mixins.ListModelMixin,
        generics.GenericAPIView
    ):
    serializer_class = CommentSerializer

    # 데이터를 가지고 오는 곳
    def get_queryset(self):
        product_id = self.kwargs['product_id']
        if product_id:
            return Comment.objects.filter(product_id=product_id).order_by('-id')
        return Comment.objects.none()
    
    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)


    
   

class ProductListView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    generics.GenericAPIView
    ):
    serializer_class = ProductSerializer
    pagination_class = ProductLargePagination

    def get_queryset(self):
        product = Product.objects.all()
        name = self.request.query_params.get('name')
        if name:
            product = product.filter(name__contains=name)
        return product.order_by('id')
    
    def get(self, request, *args, **kwargs):
        print(request.user)
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class ProductDetailView(
        mixins.RetrieveModelMixin,
        mixins.DestroyModelMixin,
        mixins.UpdateModelMixin,
        generics.GenericAPIView
    ):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')
    
    def get(self, request, *args, **kwargs):
        print(request.user)
        return self.retrieve(request, args, kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, args, kwargs)
    