from django.urls import path
from cartapp import views

urlpatterns = [

    path('cartdetails',views.cartdetails,name='cartdetails'),
    path('addcart/<int:product_id>', views.add_cart, name='addcart'),
    path('cart_decrement/<int:product_id>', views.min_cart, name='cart_decrement'),
    path('remove/<int:product_id>', views.delete_cart, name='remove'),
    path('checkout', views.Checkout, name='checkoutpage')

]
