from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_order = request.GET.get('sort')
    if sort_order == 'max_price':
        phones = reversed(Phone.objects.order_by('price'))
    elif sort_order == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sort_order == 'name':
        phones = Phone.objects.order_by('name')
    else:
        phones = Phone.objects.all()

    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = list(Phone.objects.filter(slug=slug))
    context = {
        'phone': phone[0]
    }
    return render(request, template, context)
