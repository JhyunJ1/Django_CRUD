# 2023-shinhan
### Django에서 REST를 썼을 경우 차이점

- url.py를 app 폴더 안에도 생성해 나눠써 코드를 최적화함
- app을 생성했을 때 serializers, paginations 파일을 따로 생성
- **GET, POST 이름으로 함수 생성 시, 자동으로 GET POST 기능에 연결**
- queryset, pagination, serializer을 get post에서 공유해서 사용
- serializer : 객체를 json으로 변환할 때 문자열이 아니어도 다 json으로 변환해줌
- mixin : (어떤 함수가 있다는 가정 하에) 기능 제공 (list로 get, 하나만 get, post ..)
