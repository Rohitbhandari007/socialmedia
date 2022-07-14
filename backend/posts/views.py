from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status

from .models import Post
from .serializers import PostSerializer, PostViewSetSerializer


@api_view(['GET'])
def home(request):

    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)

    return Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostViewSetSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostViewSetSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        messege = {"messege": "deleted item"}
        postid = self.get_object.id
        print(instance)
        return Response(messege, status=status.HTTP_204_NO_CONTENT)


class LikeUnlikePost(APIView):

    def post(self, request):
        pk = request.data.get('pk')
        post = get_object_or_404(Post, id=pk)

        print(request.user)

        if request.user in post.liked.all():
            liked = False
            post.liked.remove(request.user)
        else:
            liked = True
            post.liked.add(request.user)

        return Response({
            'liked': liked,
            'count': post.like_count
        })
