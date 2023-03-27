from django.shortcuts import render, redirect

from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):

    sort_by = request.GET.get('sort')

    if sort_by == 'name':
        all = Phone.objects.all().order_by('name')
    elif sort_by == 'min_price':
        all = Phone.objects.all().order_by('price')
    elif sort_by == 'max_price':
        all = Phone.objects.all().order_by('-price')
    else:
        all = Phone.objects.all()

    template = 'catalog.html'

    context = {
        'phone': all
    }
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.filter(slug = slug).first()

    template = 'product.html'

    context = {
        'product': phone
    }

    return render(request, template, context)
