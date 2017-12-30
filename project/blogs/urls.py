from django.conf.urls import url
from .views import *
from posts.views import NewPost
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^list/(?P<page>\d+)/$', BlogList.as_view(), name='blog_list'),
    url(r'^(?P<pk>\d+)/$', BlogDetail.as_view(), name='blog_detail'),
    url(r'^new/$', login_required(NewBlog.as_view()), name='new_blog'),
    url(r'^(?P<pk>\d+)/addpost/$', login_required(NewPost.as_view()), name='new_post'),
]