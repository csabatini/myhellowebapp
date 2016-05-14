from django.shortcuts import render
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
