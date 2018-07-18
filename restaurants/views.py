from django.shortcuts import render
from .models import Restaurant

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    context = {
        "my_list": Restaurant.objects.all()
        
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):
    context = {
        "my_object":Restaurant.objects.all,
    }
    return render(request, 'detail.html', context)
