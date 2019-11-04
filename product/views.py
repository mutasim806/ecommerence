from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from cart.forms import CartAddProductForm
from .forms import *
from django.contrib.auth.models import User
from product.utils import get_ecommerence_context_data
from .models import *


class ShowView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = get_ecommerence_context_data()
        return render(request, self.template_name, context)


class DetailsView(LoginRequiredMixin, View):
    permission_required = ''
    template_name = 'product_details.html'

    def get(self, request, id):
        # product = Product.objects.get(id=id)
        detail_images = Images.objects.filter(product_id=id)
        main_img = Images.objects.filter(product_id=id).first()
        details = ProductDetails.objects.get(product_id=id)
        specs = Specifications.objects.filter(product_id=id)
        desc = Description.objects.filter(product_id=id)
        cap = Capacity.objects.filter(product_id=id)
        context = get_ecommerence_context_data()
        # context['pro'] = product
        context['detail_images'] = detail_images
        context['main_img'] = main_img
        context['details'] = details
        context['specs'] = specs
        context['desc'] = desc
        context['cap'] = cap
        context['product_id'] = id
        context['cart_product_form'] = CartAddProductForm()
        return render(request, self.template_name, context)
