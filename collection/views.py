from django.shortcuts import render


def index(request):
    number = 6
    return render(request, 'index.html', {
        'number': number,
    })
