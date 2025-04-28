from django.urls import path
from .views import *

urlpatterns =  [
    path("", post_list, name="post_list"),
    path("post-create/", create_post, name="post_create"),
    path("post/<pk>/", post_detail, name="post-detail"),
    path("post-update/<pk>/", post_update, name="post-update"),
    path("post-delete/<pk>/", post_delete, name="post-delete"),
    
]