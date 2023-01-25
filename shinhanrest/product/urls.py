from django.urls import path
from . import views

urlpatterns = [
    # Generic view에 의해 pk라고 설정
    path("/<int:pk>", views.ProductDetailView.as_view()),
    path("/<int:product_id>/comment", views.CommentListView.as_view()),
    path("/comment", views.CommentCreateView.as_view()),
    path("/like", views.LikeCreateView.as_view()),
    path("", views.ProductListView.as_view()),
]   
