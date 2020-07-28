from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from sitemap.models import Blog


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def blog(request, identifier):
    item = get_object_or_404(Blog, identifier=identifier)

    context = {'blog': item}
    return render(request, 'sitemap/blog.html', context)