from django.shortcuts import get_object_or_404, render
from .models import Blog, Category

# Create your views here.
def posts_by_category(request, category_id):
    posts = Blog.objects.filter(category_id=category_id, status='published')
    category = get_object_or_404(Category, id=category_id)
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)