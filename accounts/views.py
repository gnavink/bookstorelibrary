# This file is redundant now as the authentication is done by django-allauth package. The file can be deleted
from django.views import generic
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm


class SignUpPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
