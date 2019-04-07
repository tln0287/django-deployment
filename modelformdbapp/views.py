from django.shortcuts import render
from .forms import ProductForm
from .models import Product
def input(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'links.html')
    else:
        form = ProductForm()
    return render(request, 'data.html', {'form': form})
def display(request):
    recs=Product.objects.all()
    return render(request,'display.html',{'records':recs})

