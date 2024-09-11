import os
import stripe
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Product

stripe.api_key = os.environ.get('STRIPE_API_KEY')
PORTAL_DOMAIN = os.environ.get('PORTAL_DOMAIN')

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
            success_url=f'{PORTAL_DOMAIN}/success.html',
            cancel_url=f'{PORTAL_DOMAIN}/cancel.html'
        )
    except Exception as e:
        return HttpResponse(str(e), status=400)
    
    return redirect(checkout_session.url, 303)