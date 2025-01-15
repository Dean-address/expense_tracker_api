from django.urls import path
from .apis import ActivateUser


from django.urls import path, include
from rest_framework.routers import DefaultRouter


app_name = "authentication"

urlpatterns = [
    path(
        "activate/<str:uid>/<str:token>",
        ActivateUser.as_view({"get": "activation"}),
        name="activation",
    ),
]
