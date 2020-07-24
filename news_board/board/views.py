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


# todo add pagination and ordering by id
class CommentsListView(APIView):
    """Handling list of comments and creation of comment"""

    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentsListSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        comment = CommentSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
        return Response(status=HTTP_201_CREATED, data=comment.data.get("id"))


class CommentView(APIView):
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


class PostListView(APIView):
    """Handling list of posts and creation of post"""

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostsListSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        post = PostSerializer(data=request.data)
        if post.is_valid():
            post.id = request.data["id"]
            return Response(status=HTTP_201_CREATED, data=post.data.get("id"))
        return Response(status=HTTP_400_BAD_REQUEST, data=post.data.get("id"))


class PostView(APIView):
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

    post = Post.objects.get(id=pk)
    post.amount_of_upvotes += 1
    post.save()
    return Response(status=HTTP_200_OK)

