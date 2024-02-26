from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage.html')


def books(request):
    return render(request, 'books.html')


def contact(request):
    return render(request, 'contact.html')


def cart(request):
    return render(request, 'cart.html')


def login(request):
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')