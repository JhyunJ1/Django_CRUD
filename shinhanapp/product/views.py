from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Product

# Create your views here.

# templates 폴더 만들고 product.html => 여기에 상품 리스트 표시되게
# main 함수 만들어서 상품 리스트 나오게 하기
# 상품 리스트에는 한줄로 상품명, 가격, 장소 나오게 하기

def main(request):
    products = Product.objects.all()
    return render(request, 'product.html', { 'products': products })

def write(request):
    return render(request, 'product_write.html')

def detail(request, pk):
    product = Product.objects.get(pk=pk)

    return JsonResponse({
        'title': product.title,
        'content': product.content,
        'price': product.price,
        'location': product.location,
    })