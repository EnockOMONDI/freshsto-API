
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from account.models import Client

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            client=Client.objects.get(user=request.user)
           
               
                

           
            order.save()
           
            client.no_of_orders+=1
            client.save()
            print(client.no_of_orders)
            
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
           
            discount=order.get_discount(client)
            print(discount)
            print(order.get_total_cost())
            total_cost = order.get_total_cost()
        return render(request, 'orders/order/created.html',  {
            'order': order,
            'total_cost': total_cost ,
            'discount':  discount,
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
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/createorder.html', {
        
        'form': form,
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