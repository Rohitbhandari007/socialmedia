from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Post
from .serializers import PostSerializer


@api_view(['GET'])
def home(request):


    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)

    return Response(serializer.data)


class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)



@api_view(['POST'])
def like_unlike_post(request):
    if request.method == 'POST':
        pk = request.data.get('pk')
        post = get_object_or_404(Post, id=pk)

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

