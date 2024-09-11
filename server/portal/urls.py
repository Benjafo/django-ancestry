from django.urls import path
from . import views

app_name = 'portal'
urlpatterns = [
    path('checkout/<int:product_id>/', views.create_checkout_session, name='create_checkout_session'),
]