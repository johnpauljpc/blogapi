from django.urls import path
from .views import *


urlpatterns = [
    path("", PostListCreate.as_view()),
    path("post/<slug>/", PostDetail.as_view()),
]