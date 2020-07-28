### To add sitemaps
1. In settings.py add:
    `'django.contrib.sites',`
    `'django.contrib.sitemaps',`
2. Define `SITE_ID=<x>`, and then do migrations
3. Create sitemaps.py in desired django app
4. In sitemaps.py: 
```
from django.contrib.sitemaps import Sitemap
from sitemap.models import Blog

class BlogSitemap(Sitemap):
    def items(self):
        return Blog.objects.all()
```
5.  in project/urls.py:
```
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from sitemap.sitemaps import BlogSitemap

sitemaps = {
    'blogs': BlogSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('', include('sitemap.urls')),
    
]
```
6. In your models.py add this to the model you want to include in sitemap, a unique identifier is prefferred or we can also sluggify the title and use it as identifier
```
from django.urls import reverse
def get_absolute_url(self):
        return reverse("blog", args=[(self.identifier)])
```

7. create templates/yourapp/blog.html for displaying blogs
8. create POST VIEW in yourapp/views.py
```
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from sitemap.models import Blog
def blog(request, identifier):
    item = get_object_or_404(Blog, identifier=identifier)

    context = {'blog': item}
    return render(request, 'sitemap/blog.html', context)
```