from rest_framework import serializers

from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializes single comment
    """
    class Meta:
        model = Comment
        fields = "__all__"


class CommentsListSerializer(serializers.ModelSerializer):
    """
    Serializes list of comments
    """
    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    """
    Serializes single post
    """
    class Meta:
        model = Post
        fields = "__all__"


class PostDetailSerializer(PostSerializer):
    """
    Serializes single post with attaching to it relating comments
    """

    comments = CommentsListSerializer(many=True)


class PostsListSerializer(serializers.ModelSerializer):
    """
    Serializes list of posts
    """
    class Meta:
        model = Post
        fields = "__all__"
