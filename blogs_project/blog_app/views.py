
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Blog
from django import forms
from django.urls import reverse_lazy



def all_blogs(request):
   blogs = Blog.objects.order_by('-date')
   category_search = Blog.objects.values_list('category',flat=True).distinct()
   selected_blogs = ''
   category = ''
   if 'category' in request.GET:
      category = request.GET['category']
      if category:
         selected_blogs = blogs.filter(category__iexact=category)


   data = {
      'blogs':blogs,
      'categories':category_search,
      'selected_blogs':selected_blogs,
      'category':category
   }

   return render(request, 'blog/all_blogs.html',data)

def detail(request, pk):
   blog = get_object_or_404(Blog, pk=pk)
   blogs = Blog.objects.order_by('-date')
   
   data = {
      'blog':blog,
      'blogs':blogs,
   }

   return render(request, 'blog/detail.html', data)

