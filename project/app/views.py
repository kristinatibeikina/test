from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .models import *
from .forms import *


# Create your views here.

class ContactsTemplateView(TemplateView):
    template_name = 'contacts.html'

class AboutTemplateView(TemplateView):
    template_name = 'about.html'

class CreateProductView(LoginRequiredMixin, CreateView):
    template_name = 'add_product.html'
    form_class = CreateProductForm
    model = Product
    success_url = reverse_lazy('add_product')

class ProductListView(ListView):
    template_name = 'products.html'
    model = Product
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'

