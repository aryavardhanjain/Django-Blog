from django.shortcuts import render
from blogs.models import Category, Blog, About

def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status='published').order_by('-updated_at')
    posts = Blog.objects.filter(is_featured=False, status='published').order_by('-updated_at')
    try:
        about = About.objects.get()
    except:
        about = None
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about
    }
    return render(request, 'home.html', context)