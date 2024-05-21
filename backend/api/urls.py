from django.urls import path
from .views import RegisterUser, LoginUser
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("register", RegisterUser.as_view(), name="register"),
    path("login", LoginUser.as_view(), name="login"),
    path("token/refresh/", TokenObtainPairView.as_view(), name="token_refresh")
]