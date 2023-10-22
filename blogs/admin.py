from django.contrib import admin
from django.http.request import HttpRequest
from .models import Category, Blog, About, SocialLink, Comment

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title', )}
    list_display = ('title', 'category', 'author', 'is_featured', 'status')
    search_fields = ('id', 'title', 'category__category_name', 'status')

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        else:
            return False
        

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)
admin.site.register(Comment)