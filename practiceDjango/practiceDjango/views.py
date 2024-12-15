from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Hello, World!')
    return render(request, 'index.html')

def about(request):
    # return HttpResponse('About page')
    return render(request, 'websites/about.html')

def contact(request):
    return HttpResponse('Contact page')