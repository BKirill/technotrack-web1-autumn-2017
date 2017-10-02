from django.shortcuts import render

# Create your views here.

def mainpage(request):

    return render(request, 'mainpage.html')

def blogs_list(request):

    return render(request, 'blogs_list.html')

def posts_list(request, name = None):

    return render(request, 'posts_list.html', {'name': name})

def view_post(request, name = None, post = None):

    return render(request, 'view_post.html', {'name': name, 'post': post})

def profile(request, name = None):

    return render(request, 'profile.html', {'name': name})