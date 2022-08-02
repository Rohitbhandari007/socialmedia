from django.urls import path, include
from .views import profilePost, PostViewSet, LikeUnlikePost
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")


urlpatterns = [
    path('', profilePost, name='home'),
    path('', include(router.urls)),
    path('like-unlike/', LikeUnlikePost.as_view(), name='like-unlike')

]
