from django.conf.urls import url
from .views import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', MainPageView.as_view(), name="mainpage"),
    url(r'^profile/(?P<pk>\d+)/$', UserProfile.as_view(), name='user_profile'),
    url(r'^myprofile/$', login_required(MyProfile.as_view()), name='my_profile'),
    url(r'^login/$', LoginView.as_view(template_name='core/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', Register.as_view(), name='register'),
]