from django.views.generic import ListView, CreateView
from django.views.generic import DetailView
from .models import Blog
from django.shortcuts import reverse
from django import forms


class BlogListForm(forms.Form):

    order_by = forms.ChoiceField(choices=(
        ('title', 'Title asc'),
        ('-title', 'Title desc'),
        ('author', 'Author asc'),
        ('-author', 'Author desc')
    ), required=False)
    search = forms.CharField(required=False)


class BlogList(ListView):

    template_name = 'blogs/blogs_list.html'
    model = Blog
    paginate_by = 3

    def get_queryset(self):
        q = super(BlogList, self).get_queryset()
        self.form = BlogListForm(self.request.GET)
        if self.form.is_valid():
            if self.form.cleaned_data['order_by']:
                q = q.order_by(self.form.cleaned_data['order_by'])
            if self.form.cleaned_data['search']:
                q = q.filter(title__contains=self.form.cleaned_data['search'])
        return q

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context


class BlogDetail(DetailView):

    template_name = 'blogs/blog_detail.html'
    context_object_name = 'blog'
    model = Blog

    def get_queryset(self):
        return super(BlogDetail, self).get_queryset().select_related()

    def get_context_data(self, **kwargs):

        context = super(BlogDetail, self).get_context_data(**kwargs)
        context['available_posts'] = self.object.posts.available_for_user(self.request.user)
        return context


class NewBlog(CreateView):

    template_name = 'blogs/new_blog.html'
    model = Blog
    fields = 'title', 'description'

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NewBlog, self).form_valid(form)