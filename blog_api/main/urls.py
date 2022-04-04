from django.urls import path
from . import views

urlpatterns = [
    path("posts/",  views.posts),
    path("posts/<int:post_id>",  views.post_detail)
]
