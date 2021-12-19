from django.shortcuts import render,redirect
from .models import *
# from config.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.views.generic.list import ListView
from django.views.generic import TemplateView,DetailView,View
from rest_framework.decorators import api_view
from rest_framework.views import Response
# from .serial import *


class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        product = Product.objects.all()
        context = {"category":category,"product":product}
        return context

class AboutUs(TemplateView):
    template_name = 'index-1.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        context = {"category":category}
        return context


class CategoryView(View):
    def get(self,request,cat_slug):
        try:
            category = Category.objects.get(slug=cat_slug)
        except:
            return render(request,'404.html')
        posts = category.products.all()
        categories = Category.objects.all()
        context = {'categories':categories,"posts":posts}
        return render(request,'products.html',context)

class ProductView(TemplateView):
    template_name = 'index-2.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        product = Product.objects.all()
        context = {"category":category,"product":product}
        return context

class ServiceView(TemplateView):
    template_name = 'index-3.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoty = Category.objects.all()
        product = Product.objects.all()[1:]
        products = Product.objects.all()[5:]
        context = {"categoty":categoty,"product":product,'products':products}
        return context

class MenuView(TemplateView):
    template_name = 'index-4.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        product = Product.objects.all()[5:]
        context = {'category':category,'product':product}
        return context

class ContactView(TemplateView):
    template_name = 'index-5.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        context = {"category":category}
        return context

