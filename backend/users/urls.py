from django.urls import path
from users.views import UserRegestrationView, UserLoginView, UserProfileView, FollowUnfollow, ChangePasswordView

urlpatterns = [
    path('register/', UserRegestrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('changepassword/', ChangePasswordView.as_view(), name='changepassword'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('follow-unfollow/', FollowUnfollow.as_view(), name='follow-unfollow')
]
