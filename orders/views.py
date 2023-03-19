
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
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
            'local_css_urls' : settings.SB_ADMIN_3_CSS_LIBRARY_URLS,
            'local_js_urls' : settings.SB_ADMIN_3_JS_LIBRARY_URLS
          })
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/createorder.html', {
        
        'form': form,
        'local_css_urls' : settings.SB_ADMIN_3_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_3_JS_LIBRARY_URLS
          })