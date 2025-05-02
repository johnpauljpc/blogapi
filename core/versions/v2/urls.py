from django.urls import path
from .views import *

urlpatterns = [
    path("", ListCreatePost.as_view(), name="list_create_post"),
    path("post/<slug>/", PostDetail.as_view(), name="detail"),
]