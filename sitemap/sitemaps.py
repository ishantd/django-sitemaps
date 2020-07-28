from django.contrib.sitemaps import Sitemap
from sitemap.models import Blog

class BlogSitemap(Sitemap):
    def items(self):
        return Blog.objects.all()