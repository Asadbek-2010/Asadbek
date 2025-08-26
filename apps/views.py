from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from apps.models import Category, Product


class TestView(ListView):
    queryset = Category.objects.all()
    template_name = 'parts/index.html'
    context_object_name = 'categories'


    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['products'] = Product.objects.all()
        return ctx



# Create your views here.
class Catalog(TemplateView):
    template_name = 'parts/catalog.html'

class Cart(TemplateView):
    template_name = 'parts/cart.html'

class Deals(TemplateView):
    template_name = 'parts/deals.html'

class Profile(TemplateView):
    template_name = 'parts/profile.html'

class Register(TemplateView):
    template_name = 'parts/Register Page.html'

class Logging(TemplateView):
    template_name = 'parts/Login Page.html'

class Products(TemplateView):
    template_name = 'parts/product.html'