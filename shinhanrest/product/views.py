from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Product, Comment, Like
from .serializers import (
    ProductSerializer,
    CommentSerializer,
    CommentCreateSerializer,
    LikeCreateSerializer
)
from .paginations import ProductLargePagination

### CRUD <Create Read Upgrade Delete>

class LikeCreateView(
        mixins.CreateModelMixin,
        generics.GenericAPIView
    ):
    serializer_class = LikeCreateSerializer

    # 데이터를 가지고 오는 곳
    def get_queryset(self):
        return Like.objects.all()
    
    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product')

        if Like.objects.filter(member=request.user, product_id=product_id).exists():
            Like.objects.filter(member=request.user, product_id=product_id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return self.create(request, args, kwargs)


class CommentCreateView(
        mixins.CreateModelMixin,
        generics.GenericAPIView
    ):
    serializer_class = CommentCreateSerializer

    def get_queryset(self):
        return Comment.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class CommentListView(
        mixins.ListModelMixin,
        generics.GenericAPIView
    ):
    serializer_class = CommentSerializer

    # 데이터를 가지고 오는 곳
    def get_queryset(self):
        product_id = self.kwargs['product_id']
        if product_id:
            return Comment.objects.filter(product_id=product_id).select_related('member', 'product').order_by('-id')
        ## Comment.objects.filter(product__pk=1) : product 안에 pk가 1인 상품
        ## Comment.objects.filter(product__product_type='단품') : product 안에 product_type이 단품이 상품
        return Comment.objects.none()
    
    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)


class ProductListView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    generics.GenericAPIView
    ):
    # generics.GenerciAPIView 안에 lookup_filed = 'pk'로 설정되어서 경로를 /<int:pk>로 설정
    serializer_class = ProductSerializer
    pagination_class = ProductLargePagination
    #permission_classes = [IsAuthenticated] # function 마다 로그인 확인하지 않기 위해 클래스에 선언

    def get_queryset(self):
        product = Product.objects.all().prefetch_related('comment_set')
        name = self.request.query_params.get('name')
        if name:
            product = product.filter(name__contains=name)
        return product.order_by('id')
    
    def get(self, request, *args, **kwargs):
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

