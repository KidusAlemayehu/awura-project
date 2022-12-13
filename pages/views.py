from django.shortcuts import render
from products.models import Product

# Create your views here.
def landing(request):
    # qs = Product.objects.all()
    # data={
    #     "products": qs
    # }
    return render(request,'index.html')