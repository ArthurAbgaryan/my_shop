from django.shortcuts import render
from .models import Product,Category
from django.shortcuts import get_object_or_404
from cart.forms import CartAddProductForm

def list_products(request, category_slug=None):
    category = None
    context = {}
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = products.filter(category = category)
    context['category'] = category
    context['products'] = products
    context['categories'] = categories
    return render(request, 'shop/list_products.html', context)

def products_detail(request, slug, pk):
    product = get_object_or_404(Product, slug = slug, id = pk,available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product_detail.html', {'product':product,
                                                        'cart_product_form':cart_product_form})

# Create your views here.
