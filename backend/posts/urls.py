from django.urls import path, include
from .views import profilePost, PostViewSet, LikeUnlikePost, UserProfilePostView, CommentView, ListComment
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")


urlpatterns = [
    path('', profilePost, name='home'),
    path('', include(router.urls)),
    path('like-unlike/', LikeUnlikePost.as_view(), name='like-unlike'),
    path('profile-post/', UserProfilePostView.as_view(), name='profile-post'),
    path('comment/', CommentView.as_view(), name='comment-view'),
    path('list-comment/', ListComment.as_view(), name='list-comment')


]
