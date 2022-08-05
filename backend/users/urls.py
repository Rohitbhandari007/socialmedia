from django.urls import path
from users.views import UserRegestrationView, UserLoginView, UserPublicProfileView, UserListView, UserProfileView, FollowUnfollow, UserChangePasswordView, SendPasswordResetEmailView, UserPasswordResetView, SuggestionsView

urlpatterns = [
    path('register/', UserRegestrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('userlist/', UserListView.as_view(), name='profile'),
    path('userprofile/', UserPublicProfileView.as_view(), name='userprofile'),
    path('suggestions/', SuggestionsView.as_view(), name='suggestions'),
    path('follow-unfollow/', FollowUnfollow.as_view(), name='follow-unfollow'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(),
         name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/',
         UserPasswordResetView.as_view(), name='reset-password'),
]
