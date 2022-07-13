from django.urls import path, include
from .views import home, PostViewSet, LikeUnlikePost
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")


urlpatterns = [
    path('', home, name='home'),
    path('', include(router.urls)),
    path('like-unlike/', LikeUnlikePost.as_view(), name='like-unlike')

]
