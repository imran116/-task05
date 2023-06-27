from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView, UpdateView

from inventory import forms
from inventory.models import Category, Product


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'


class AddCategoryView(CreateView):
    form_class = forms.CategoryForm
    template_name = 'add-category.html'
    queryset = Category.objects.all()
    success_url = '/category/list/'


class ListCategoryView(ListView):
    template_name = 'list_category.html'
    queryset = Category.objects.all()
    context_object_name = 'categoryObj'


class EditCategoryView(UpdateView):
    form_class = forms.CategoryForm
    template_name = 'edit-category.html'
    queryset = Category.objects.all()
    success_url = '/category/list/'
    pk_url_kwarg = 'pk'


class DeleteCategoryView(View):
    def get(self, request, pk):
        instance = Category.objects.get(pk=pk)
        instance.delete()
        return redirect('/category/list/')


class ListProductView(ListView):
    template_name = 'list_product.html'
    queryset = Product.objects.all()
    context_object_name = 'productObj'


class AddProductView(CreateView):
    form_class = forms.ProductForm
    template_name = 'add-product.html'
    queryset = Product.objects.all()
    success_url = '/product/list/'


class EditProductView(UpdateView):
    form_class = forms.ProductForm
    template_name = 'edit-product.html'
    queryset = Product.objects.all()
    success_url = '/product/list/'
    pk_url_kwarg = 'pk'


class DeleteProductView(View):
    def get(self, request, pk):
        instance = Product.objects.get(pk=pk)
        instance.delete()
        return redirect('/product/list/')
