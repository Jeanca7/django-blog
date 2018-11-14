#this urls was created in blog
from django.urls import path
from blog.views import repost_detail, edit_post, write_post, get_unpublished_posts, publish_post

urlpatterns=[
    path('<int:id>/', repost_detail, name='repost_detail'),
    path('unpublished', get_unpublished_posts, name='get_unpublished_posts'),
    path('<int:id>/edit/',  edit_post, name='edit_post'),
    path('write_post/',  write_post, name='write_post'),
    path('<int:id>/publish/', publish_post, name='edit_post'),
    ]