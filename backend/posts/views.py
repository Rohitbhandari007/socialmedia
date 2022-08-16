from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, exceptions
from .permissions import OnlyAuthor

from .models import Post, Comment
from .serializers import PostSerializer, PostViewSetSerializer, CommentSerializer


@api_view(['GET'])
def profilePost(request):

    posts = Post.objects.filter(author=request.user).order_by('-id')
    context = {'user': request.user}
    serializer = PostSerializer(posts, context=context, many=True)
    return Response(serializer.data)


class UserProfilePostView(APIView):

    def post(self, request):
        uid = request.data.get('uid')
        posts = Post.objects.filter(author=uid).order_by('-id')
        context = {'user': request.user}

        serializer = PostSerializer(posts, context=context, many=True)
        return Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer
    permission_classes = [OnlyAuthor]

    def list(self, request):
        queryset = Post.objects.all().order_by('-id')
        context = {'user': self.request.user}
        serializer = PostSerializer(queryset, context=context, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        instance = self.get_object()
        context = {'user': self.request.user}
        serializer = self.get_serializer(instance, context=context)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        message = {'Messege': 'Item deleted succesfully'}
        return Response(message, status=status.HTTP_204_NO_CONTENT)


class LikeUnlikePost(APIView):

    def post(self, request):
        pk = request.data.get('pk')
        post = get_object_or_404(Post, id=pk)

        print("hello")

        print(request.user)

        if request.user in post.liked.all():
            liked = False
            post.liked.remove(request.user)
        else:
            liked = True
            post.liked.add(request.user)

        return Response({
            'liked': liked,
            'count': post.like_count,

        })


class CommentView(APIView):

    def get_object(self, pk):
        post = Post.objects.get(id=pk)
        return post

    def get(self, request):
        pk = request.data.get('pk')
        print('post id : ')
        print(pk)
        post = self.get_object(pk=pk)
        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        pk = request.data.get('pk')
        body = request.data.get('body')
        post = self.get_object(pk=pk)

        if len(body) < 1:
            raise exceptions.APIException('Can not be blank')
        new_comment = Comment(body=body, author=request.user, post=post)
        new_comment.save()
        serializer = CommentSerializer(new_comment)
        return Response(serializer.data)
