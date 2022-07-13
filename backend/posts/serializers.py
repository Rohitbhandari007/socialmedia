from rest_framework import serializers
from .models import Post
from users.serializers import UserProfileSerializer, UserSerializer


class PostSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(read_only=True)
    like_count = serializers.SerializerMethodField(read_only=True)
    liked = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def get_like_count(self, obj):
        return obj.liked.count()


class PostViewSetSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
