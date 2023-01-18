from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product

# CRUD
# Create Read Update Delete

class ProductListView(APIView):

    def post(self, request, *args, **kwargs):
        product = Product(
            # name = request.data.get('name),
            name = request.data['name'],
            price = request.data['price'],
            product_type = request.data['product_type'],
        )
        product.save() # db에 저장 - 이 때 primary key가 만들어짐
        return Response({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'product_type': product.product_type,
        }, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        ret = []
        # QuerySet
        # price
        product = Product.objects.all()
        
        if 'price' in request.query_params:
            price = request.query_params['price']
            product = product.filter(price__lte=price)

        if 'name' in request.query_params:
            name = request.query_params['name']
            product = product.filter(name__contains=name)

        product = product.order_by('id')

        # name에 전달된 값이 포함된 상품을 검색 (filter)한 결과
        # 포함된을 표현하는 방법 __contains

        for p in product:
            ret.append({
                'id': p.id,
                'name': p.name,
                'price': p.price,
                'product_type': p.product_type,
            })
            
        
        return Response(ret)

class ProductDetailView(APIView):
    def put(self, request, pk, *args, **kwargs):
        product = Product.objects.get(pk=pk)

        dirty = False
        for key, value in request.data.items():
            # (+) 보안
            if key not in [f.name for f in product._meta.get_fields()]:
                continue

            dirty = dirty or value != getattr(product, key)
            setattr(product, key, value)
        
        if dirty:   
            product.save()

        return Response()

    def delete(self, request, pk, *args, **kwargs):

        # 1. 없으면 지워졌다고 거짓말 하기 (204 반환)
        # 2. 없으면 없다고 반환하기 (404 반환)

        if Product.objects.filter(pk=pk).exists():
            product = Product.objects.get(pk = pk)
            product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, pk,*args, **kwargs) :

        # 1. get 하기 전에 exists()로 확인하고 가져오기
        # 2. get 할 때 예외처리 하기

        try:        
            product = Product.objects.get(pk = pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        ret = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'product_type': product.product_type,
        }
        
        return Response(ret)
