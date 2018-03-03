from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.template import loader
from django.utils import timezone
from .models import Post

#Create your views here.

# def post_list(request):
#     template = loader.get_template('blog/post_list.html')
#     context = { 'name': 'ME'
#     }
#     return HttpResponse(template.render(context, request))

Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')


def post_list(request):
    template = loader.get_template('blog/post_list.html')
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context = { 'name': 'ME'}
    return HttpResponse(template.render(context, request))