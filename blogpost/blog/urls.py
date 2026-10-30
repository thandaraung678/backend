
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from .views import CategoryViewSet
from .views import PostViewSet
from .views import CommentViewSet
from .views import UserProfileViewSet
from .views import TagViewSet
from .views import PostTagViewSet
from .views import PostLikeViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'tags', TagViewSet)
router.register(r'posttags', PostTagViewSet)
router.register(r'postlikes', PostLikeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
