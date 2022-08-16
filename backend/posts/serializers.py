from rest_framework import serializers
from .models import Post, Comment
from users.models import User
from users.serializers import UserProfileSerializer, UserSerializer


class PostSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(read_only=True)
    like_count = serializers.SerializerMethodField(read_only=True)
    liked = UserSerializer(many=True, read_only=True)
    iliked = serializers.SerializerMethodField(read_only=True)
    comment_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def get_like_count(self, obj):
        return obj.liked.count()

    def get_iliked(self, obj):
        return True if self.context.get('user') in obj.liked.all() else False

    def get_comment_count(self, obj):
        return obj.parent_post.count()


class PostViewSetSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    iliked = serializers.SerializerMethodField(read_only=True)
    like_count = serializers.SerializerMethodField(read_only=True)
    created = serializers.DateTimeField(format='%B %d %Y %I:%M %p')

    class Meta:
        model = Comment
        fields = '__all__'

    def get_iliked(self, obj):
        return True if self.context.get('user') in obj.liked.all() else False

    def get_like_count(self, obj):
        return obj.liked.count()
