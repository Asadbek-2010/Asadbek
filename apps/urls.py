from django.urls import include
from django.urls import path

from apps.views import TestView, Catalog, Cart, Deals, Profile, Register, Logging, Products

urlpatterns = [

    path('', TestView.as_view(), name='main-page'),
    path('cart/', Cart.as_view(), name='cart-page'),
    path('catalog/', Catalog.as_view(), name='catalog-page'),
    path('deals/', Deals.as_view(), name='deals-page'),
    path('profile/', Profile.as_view(), name='profile-page'),
    path('register/', Register.as_view(), name='register-page'),
    path('login/', Logging.as_view(), name='logging-page'),
    path('product/', Products.as_view(), name='product-page'),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]
