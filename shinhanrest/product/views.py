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
        product = Product.objects.all().order_by('-id')

        ret = []

        for p in product:
            ret.append({
                'name': p.name,
                'price': p.price,
                'product_type': p.product_type,
            })
            
        
        return Response(ret)

class ProductDetailView(APIView):
    def delete(self, request, pk, *args, **kwargs):
        pass

    def get(self, request, pk,*args, **kwargs) :
        product = Product.objects.get(pk = pk)

        ret = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'product_type': product.product_type,
        }
        
        return Response(ret)
