from django.urls import re_path

from .views import registration, login, logout_user

urlpatterns = [
    re_path("registration/", registration, name="reg"),
    re_path("login/", login, name="login"),
    re_path("logout/", logout_user, name="logout"),
]
