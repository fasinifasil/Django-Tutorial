from django.urls import path
from . import views
urlpatterns =[
    path('',views.store,name='storepage'),
    path('cart', views.cart, name='cartpage'),
    path('checkout', views.checkout, name='checkoutpage'),

]