import stripe
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Product

stripe.api_key = 'sk_test_51PxYt9KsX8iFIbQ65B3pDup2ufCUCBadwMWw5PwUN4uydWjxgyLaGkLs07HGhYe6OJosqLGAAZOuPCcjo4Bs3yKH001aaa8jRU'
DOMAIN = 'http://localhost:8000/api/portal'

# Create your views here.
def create_checkout_session(request, product_id, quantity=1):
    product = get_object_or_404(Product, pk=product_id)
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items = [
                {
                    'price': product.stripe_price_id,
                    'quantity': quantity
                }
            ],
            mode='payment',
            success_url=f'{DOMAIN}/success.html',
            cancel_url=f'{DOMAIN}/cancel.html'
        )
    except Exception as e:
        return HttpResponse(str(e), status=400)
    
    return redirect(checkout_session.url, 303)