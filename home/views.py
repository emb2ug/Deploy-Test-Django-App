from django.shortcuts import render


def show_welcome(request):
    return render(request, 'home.html')
