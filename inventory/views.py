from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView, UpdateView

from inventory import forms
from inventory.models import Category


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


class DeletCategoryView(View):
    def get(self, request, pk):
        instance = Category.objects.get(pk=pk)
        instance.delete()
        return redirect('/category/list/')
