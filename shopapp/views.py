from django.shortcuts import render, HttpResponse
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.

def Base(request):
    cat = Category.objects.all()
    return render(request, 'shop/base.html', {'categories': cat})


def Index(request):
    all_post = Product.objects.all()
    pagination = Paginator(all_post, 2)
    page_no = request.GET.get('page')
    page_obj = pagination.get_page(page_no)
    total_page = page_obj.paginator.num_pages
    total_page_list = [n+1 for n in range(total_page)]
    print('pagination', pagination)
    print()
    print('page_no', page_no)
    print()
    print('page_obj', page_obj)
    print()
    print('total_page', total_page)
    print()
    print('total_page_list', total_page_list)
    cat = Category.objects.all()
    return render(request, 'shop/index.html', {'post': page_obj, 'total': total_page_list,  'categories': cat})


def CategoryPage(request):
    cat = Category.objects.all()
    return render(request, 'shop/categories.html', {'cats': cat})


def About(request):
    return render(request, 'shop/about.html')


def Contact(request):
    return render(request, 'shop/contact.html')


def News(request):
    return render(request, 'shop/news.html')


def ProductView(request, cname):
    if (Category.objects.filter(name=cname)):
        products = Product.objects.filter(category__name=cname)
        return render(request, 'shop/productview.html', {'prods': products,'category':cname})

    return render(request, 'shop/productview.html')

def search(request):
    prod = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'shop/search.html', {'p':prod})

def Productdetail(request, pname):
    if(Product.objects.filter(name=pname)):
        p = Product.objects.filter(name=pname).first()
    return render(request, 'shop/productdetail.html', {'pro': p, 'product':pname})







