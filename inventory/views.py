from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView

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
