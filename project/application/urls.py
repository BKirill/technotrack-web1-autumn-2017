"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core.views import mainpage
from core.views import blogs_list
from core.views import posts_list
from core.views import view_post
from core.views import profile

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', mainpage),
    url(r'^blogs/$', blogs_list),
    url(r'^blogs/(?P<name>\d+)/posts/$', posts_list),
    url(r'^blogs/(?P<name>\d+)/posts/(?P<post>\d+)/$', view_post),
    url(r'^profile/(?P<name>\d+)/$', profile),
]
