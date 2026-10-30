
from rest_framework import viewsets
from .models import User, Category, Post, Comment, UserProfile, Tag, PostTag
from .models import PostLike
from .serializers import UserSerializer, CategorySerializer, PostSerializen
from .serializers import CommentSerializer, UserProfileSerializer
from .serializers import TagSerializer
from .serializers import PostTagSerializer
from .serializers import PostLikeSerializer
# from .models import Category
# from .serializers import CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

   
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializen


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    

class PostTagViewSet(viewsets.ModelViewSet):
    queryset = PostTag.objects.all()
    serializer_class = PostTagSerializer
    

class PostLikeViewSet(viewsets.ModelViewSet):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer
    