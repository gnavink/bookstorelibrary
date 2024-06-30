# This file is redundant now as the authentication is done by django-allauth package.The file can be deleted
from django.urls import path

from .views import SignUpPageView


urlpatterns = [
    path("signup/", SignUpPageView.as_view(), name="signup"),
]
