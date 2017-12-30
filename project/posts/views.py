from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView
from .models import Post, Like
from blogs.models import Blog
from comments.models import Comment
from django.shortcuts import reverse, get_object_or_404
from django.db import models

class PostDetail(CreateView):
    model = Comment
    template_name = 'posts/post_detail.html'
    fields = ('text', )

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.postobject = get_object_or_404(Post.objects.select_related().prefetch_related('categories').prefetch_related('comments'), id=pk)
        return super(PostDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['post'] = self.postobject
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.postobject
        return super(PostDetail, self).form_valid(form)

    def get_success_url(self):
        return reverse('posts:post_detail', kwargs={'pk': self.postobject.pk})

class PostComments(DetailView):
    model = Post
    template_name = 'posts/post_comments.html'
    context_object_name = 'post'


class NewPost(CreateView):

    template_name = 'posts/new_post.html'
    model = Post
    fields = 'title', 'text', 'categories'

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.blog = get_object_or_404(Blog, id=pk, author = self.request.user)
        return super(NewPost, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']

    def form_valid(self, form, pk = None):
        form.instance.author = self.request.user
        form.instance.blog = self.blog
        return super(NewPost, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(NewPost, self).get_context_data(**kwargs)
        return context


class PostUpdate(UpdateView):

    template_name = 'posts/edit_post.html'
    model = Post
    fields = 'title', 'text', 'categories', 'is_deleted'

    def get_queryset(self):
        return super(PostUpdate, self).get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse('posts:post_detail', kwargs={'pk': self.object.pk})


class PostAjaxLike(View):

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.post_object = get_object_or_404(Post, id=pk)
        return super(PostAjaxLike, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        if not self.post_object.likes.filter(author=self.request.user).exists():
            like = Like(author=request.user, post=self.post_object)
            like.save()
            Post.objects.all().filter(id=self.post_object.id).update(likes_count=models.F('likes_count')+1)
        return HttpResponse(Post.objects.get(id=self.post_object.id).likes_count)