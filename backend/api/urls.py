from django.urls import path
from .views import RegisterUser, LoginUser, UserInfoView, CoachCreateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("register", RegisterUser.as_view(), name="register"),
    path("login", LoginUser.as_view(), name="login"),
    path("token", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("user", UserInfoView.as_view(), name="user"),
    path("coach-profile", CoachCreateView.as_view(), name="coach-profile")
]