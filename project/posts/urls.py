from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', PostDetail.as_view(), name='post_detail'),
    url(r'^(?P<pk>\d+)/like/$', PostAjaxLike.as_view(), name='post_ajax_like'),
    url(r'^(?P<pk>\d+)/comments/$', PostComments.as_view(), name='post_comments'),
    url(r'^new/$', login_required(NewPost.as_view()), name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', login_required(PostUpdate.as_view()), name='post_edit'),
]