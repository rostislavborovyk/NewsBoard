from rest_framework import serializers

from .models import Post, Comment


class CommentsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostDetailSerializer(PostSerializer):
    """Post with comments"""
    comments = CommentsListSerializer(many=True)


class PostsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
