from django.shortcuts import render


def home(request):
    return render(request, 'connect/index.html')


def about(request):
    return render(request, 'connect/about.html')