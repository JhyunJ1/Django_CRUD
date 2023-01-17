from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
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
            if check_password(password, member.password):
                request.session['user_pk'] = member.id
                request.session['user_id'] = member.user_id
                return redirect('/')   
        
    return render(request,'login.html')

def logout(request):
    del(request.session['user_pk'])
    del(request.session['user_id'])

    return redirect('/')

def register(request):
    if request.method == 'POST':
        user_id = request.POST.get("user_id"),
        password = make_password(request.POST.get("password")),
        name = request.POST.get("name"),
        age = request.POST.get("age"),

        ## 아이디 중복의 경우
        if not Member.objects.filter(user_id=user_id).exists():
            member = Member(
                user_id = user_id,
                password = user_id,
                name = user_id,
                age = user_id,
            )
            member.save()
            return redirect('/login/')
    
    return render(request,'register.html')


