from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .models import Member

# Create your views here.


# 로그인 페이지
# 기능 1: 로그인 화면 출력
# 기능 2: 아이디, 비밀번호 입력받아서 로그인되는 것.

def login(request):
    if request.method == 'POST':
        member = Member(
            email = request.POST.get("email"),
            password = requst.POST.get("password"),
        )
        member.save()
    return render(request,'login.html')

