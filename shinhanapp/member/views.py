from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .models import Member

# Create your views here.


# 로그인 페이지
# 기능 1: 로그인 화면 출력
# 기능 2: 아이디, 비밀번호 입력받아서 로그인되는 것.

def login(request):
    if request.method == 'POST':
        user_id = request.POST.get("user_id")
        password = request.POST.get("password")

        if Member.objects.filter(user_id=user_id).exists():
            # 정보 하나를 가져올 때 사용
            member = Member.objects.get(user_id=user_id)

            # 로그인 성공
            if member.password == password:
                request.session['user_pk'] = member.id
                request.session['user_id'] = member.user_id
                return redirect('/')
        
    return render(request,'login.html')

