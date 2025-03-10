from django.urls import path
from .views import (
    PostListCreateView,
    PostDetailView,
    CommentListCreateView,
    LikePostView,
    CategoryListCreateView,
)

urlpatterns = [
    path("posts/", PostListCreateView.as_view(), name="post-list-create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("comments/", CommentListCreateView.as_view(), name="comment-list-create"),
    path("likes/", LikePostView.as_view(), name="like-post"),
    path("category/", CategoryListCreateView.as_view(), name="category-create"),
]
