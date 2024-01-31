from django.shortcuts import render

def index(request):
    return render(request, 'front/index.html')

def account(request):
    return render(request, 'front/account.html')

def checkout(request):
    return render(request, 'front/checkout.html')

def contact(request):
    return render(request, 'front/contact.html')

def products(request):
    return render(request, 'front/products.html')

def register(request):
    return render(request, 'front/register.html')

def single(request):
    return render(request, 'front/single.html')

def typo(request):
    return render(request, 'front/typo.html')
