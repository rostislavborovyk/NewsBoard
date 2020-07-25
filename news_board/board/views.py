from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .models import Post, Comment
from .serializers import (
    PostsListSerializer,
    PostSerializer,
    PostDetailSerializer,
    CommentsListSerializer,
    CommentSerializer,
)


class CommentsListView(ListAPIView):
    """
    Handling retrieving list of comments and creation of Comment
    """

    filter_backends = [OrderingFilter]
    pagination_class = PageNumberPagination
    serializer_class = CommentsListSerializer

    def get_queryset(self, *args, **kwargs):
        comments = Comment.objects.all()
        return comments

    def post(self, request):
        comment = CommentSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
        return Response(status=HTTP_201_CREATED, data=comment.data.get("id"))


class CommentView(APIView):
    """
    Handling get, put and delete methods of single Comment
    """

    def get(self, request, pk):
        comment = Comment.objects.get(id=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        comment = Comment.objects.get(id=pk)
        CommentSerializer().update(comment, request.data)
        return Response(status=HTTP_200_OK)

    def delete(self, request, pk):
        comment = Comment.objects.get(id=pk)
        comment.delete()
        return Response(status=HTTP_200_OK)


class PostListView(ListAPIView):
    """
    Handling retrieving list of posts and creation of Post
    """

    filter_backends = [OrderingFilter]
    pagination_class = PageNumberPagination
    serializer_class = PostsListSerializer

    def get_queryset(self, *args, **kwargs):
        posts = Post.objects.all()
        return posts

    def post(self, request):
        post = PostSerializer(data=request.data)
        if post.is_valid():
            post.save()
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)


class PostView(APIView):
    """
    Handling get, put and delete methods of single Post
    """

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = Post.objects.get(id=pk)
        PostSerializer().update(post, request.data)
        return Response(status=HTTP_200_OK)

    def delete(self, request, pk):
        post = Post.objects.get(id=pk)
        post.delete()
        return Response(status=HTTP_200_OK)


@api_view(["GET"])
def upvote_post(request, pk):
    """
    Increments upvotes of a single post by 1
    :param request: request from client
    :param pk: id of post to increment upvotes
    :return:
    """
    post = Post.objects.get(id=pk)
    post.amount_of_upvotes += 1
    post.save()
    return Response(status=HTTP_200_OK)
