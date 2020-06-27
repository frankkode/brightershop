from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


def home(request, category_slug=None):
    title = "BRIGHT | Home"
    products = Product.objects.filter(bestseller=True)
    category = None
    categories = Category.objects.all()
    return render(request, 'shop/home.html',
                           {'products': products,
                            'category': category,
                            'categories': categories,
                            'title': title})



def salon(request):
    title = "BRIGHT | Salon"
    return render(request, 'shop/salon.html', {'title': title})

def cleaning(request):
    title="BRIGHT| Cleaning"
    return render(request, 'shop/cleaning.html', {'title':title})

def service(request):
    title = "BRIGHT | Service"
    return render(request, 'shop/services.html', {'title': title})


def faq(request):
    title = "BRIGHT | FAQ"
    return render(request, 'shop/faq.html', {'title': title})


def about(request):
    title = "BRIGHT | About"
    return render(request, 'shop/about.html', {'title': title})


def product_list(request, category_slug=None):
    """
    Product Catalog view to display all available products
    or to display products filtered by category.
    """
    title = "BRIGHT | All Products"
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    cart_product_form = CartAddProductForm()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {'products': products,
                   'categories': categories,
                   'cart_product_form': cart_product_form,
                   'title': title})


def product_detail(request, id, slug):
    """
    Single Product view to display product detail page via ID.
    Slug passed in for urls building
    """
    title = "BRIGHT | Product Detail"
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    category = None
    categories = Category.objects.all()
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html',
                  {'product': product,
                   'category': category,
                   'categories': categories,
                   'cart_product_form': cart_product_form,
                   'title': title})


def special_offers(request):
    title = "BRIGHT | Special Offers"
    products = Product.objects.filter(special_offer=True)
    categories = Category.objects.all()
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/special_offers.html',
                           {'products': products,
                            'categories': categories,
                            'cart_product_form': cart_product_form,
                            'title': title})
