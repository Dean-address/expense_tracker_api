from django.urls import path
from .api.views import CreateUserView, LoginUserView

app_name = "user"
urlpatterns = [
    path("register/", CreateUserView.as_view(), name="register"),
    path("login/", LoginUserView.as_view(), name="login"),
]
