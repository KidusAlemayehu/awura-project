from django.shortcuts import render
from products.models import Product

# Create your views here.
def landing(request):
    return render(request,'index.html')
def services(request):
    return render(request,'services.html')
def projects(request):
    return render(request,'projects.html')
def vacancy(request):
    return render(request, 'vacancy.html')
def contact(request):
    return render(request,'contact.html')