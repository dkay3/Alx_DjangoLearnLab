# posts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView, LikePostView, UnlikePostView

router = DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'feed/', FeedView, basename='feed')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like_post'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike_post'),
]
