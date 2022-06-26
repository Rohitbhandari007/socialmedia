from rest_framework import serializers
from .models import Post
from users.serializers import UserProfileSerializer


class PostSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
