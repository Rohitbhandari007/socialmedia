from django.urls import path
from .views import home, PostView, LikeUnlikePost

urlpatterns = [
    path('', home, name='home'),
    path('posts/', PostView.as_view(), name='posts'),
    path('like-unlike/', LikeUnlikePost.as_view(), name='like-unlike')

]
