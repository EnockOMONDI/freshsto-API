from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/cartdetail.html', {
        'cart': cart,
                'local_css_urls': [ "assets/css/libs.min.css",
                            "assets/vendor/@fortawesome/fontawesome-free/css/all.min.css",
                            "assets/css/foodsto.mine209.css?v=1.0.0"],
                 'local_js_urls':  [
                            "assets/js/libs.min.js",
                            "assets/vendor/gsap/gsap.min.js",
                            "assets/vendor/gsap/ScrollTrigger.min.js",
                            "assets/js/app.js",
                            "assets/js/gsap.js",
                            "assets/js/slider.js"]

  })