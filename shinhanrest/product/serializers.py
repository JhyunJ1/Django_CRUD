from rest_framework import serializers
from .models import Product, Comment, Like
from member.models import Member
# from rest_framework.exceptions import ValidationError

# serializers 역할
# 데이터 변환 객체 -> json  형태

class ProductSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    

    def get_comment_count(self, obj): # get_필드명
        
        # 모델명_set : 자기 자신에 filter가 걸려 있는 변수 (모델 생성 시, 자동으로 생성)
        return obj.comment_set.all().count()
        # return Comment.objects.filter(product=obj).count() # 성능 문제 발생 가능
    
    def get_like_count(self, obj):
        return obj.like_set.all().count()


    class Meta:
        model = Product
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    member_username = serializers.SerializerMethodField()
    tstamp = serializers.DateTimeField(
        read_only=True, format='%Y-%m-%d %H:%M:%S'
    )

    def get_product_name(self, obj):
        return obj.product.name
    
    def get_member_username(self, obj):
        return obj.member.username

    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateSerializer(serializers.ModelSerializer):
    member = serializers.HiddenField(
        default=serializers.CurrentUserDefault(), 
        required=False
    )

    def validate_member(self, value):
        if not value.is_authenticated:
            raise serializers.ValidationError('member is required')
        return value

    class Meta:
        model = Comment
        fields = '__all__'
        # extra_kwargs = {'member': { 'required': False }}

class LikeCreateSerializer(serializers.ModelSerializer):
    member = serializers.HiddenField( # 유저의 정보가 남아있다면 로그인 유지
        default=serializers.CurrentUserDefault(), 
        required=False
    )

    def validate_member(self, value):
        value = Member.objects.get(pk=1)
        if not value.is_authenticated:
            raise serializers.ValidationError('member is required')
        return value

    class Meta:
        model = Like
        fields = '__all__'
        # extra_kwargs = {'member': { 'required': False }}