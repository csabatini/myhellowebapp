from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from collection.forms import StockForm
from collection.models import Stock

def index(request):
    number = 6
    stocks = Stock.objects.all()
    return render(request, 'index.html', {
        'number': number,
        'stocks': stocks,
    })

def stock_detail(request, slug):
    stock = Stock.objects.get(slug=slug)
    return render(request, 'stocks/stock_detail.html', {
        'stock': stock,
    })

def edit_stock(request, slug):
    stock = Stock.objects.get(slug=slug)
    form_class = StockForm

    if request.method == 'POST':
        form = form_class(data=request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('stock_detail', slug=stock.slug)
    else:
        form = form_class(instance=stock)

    return render(request, 'stocks/edit_stock.html', {
        'stock': stock,
        'form': form,
    })

def add_stock(request):
    form_class = StockForm

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.user = request.user
            stock.slug = slugify(stock.symbol)
            stock.save()
            return redirect('stock_detail', slug=stock.slug)
    else:
        form = form_class()
    return render(request, 'stocks/add_stock.html', {'form': form})
