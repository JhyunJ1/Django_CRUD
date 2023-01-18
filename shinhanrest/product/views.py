from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product

# CRUD
# Create Read Update Delete

class ProductListView(APIView):

    def post(self, request, *args, **kwargs):
        product = Product(
            name = request.data['name'],
            price = request.data['price'],
            product_type = request.data['product_type'],
        )
        product.save()
        return Response()

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
    def get(self, request, pk,*args, **kwargs) :
        product = Product.objects.get(pk = pk)

        ret = {
            'name': product.name,
            'price': product.price,
            'product_type': product.product_type,
        }
        
        return Response(ret)
