from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.core.cache import caches

from blogs.models import Blog
from comments.models import Comment
from posts.models import Post
from .models import User


class MainPageView(TemplateView):

    template_name = "core/mainpage.html"

    def get_context_data(self, **kwargs):
        cache = caches['default']
        context = super(MainPageView, self).get_context_data(**kwargs)
        blogs_num = cache.get('blogs_num')
        if blogs_num is None:
            blogs_num = Blog.objects.all().count()
            cache.set('blogs_num', blogs_num, 5)
        posts_num = cache.get('posts_num')
        if posts_num is None:
            posts_num = Post.objects.all().count()
            cache.set('posts_num', posts_num, 5)
        comments_num = cache.get('comments_num')
        if comments_num is None:
            comments_num = Comment.objects.all().count()
            cache.set('comments_num', comments_num, 5)
        context['blogs_num'] = blogs_num
        context['posts_num'] = posts_num
        context['comments_num'] = comments_num
        return context


class UserProfile(DetailView):

    template_name = 'core/profile.html'
    context_object_name = 'user'
    model = User

class MyProfile(TemplateView):

    template_name = 'core/myprofile.html'

class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)

class Register(FormView):
    form_class = CreateUser
    success_url = reverse_lazy('core:login')
    template_name = 'core/register.html'
    def form_valid(self, form):
        form.save()
        return super(Register, self).form_valid(form)
