from django.shortcuts import render

# Create your views here.
def all_practice(request):
    return render(request, 'practice/all_practice.html')