
from . import views
from django.urls import path
urlpatterns = [
    path('', views.HomeView.as_view()),
    path('category/add', views.AddCategoryView.as_view(), name='add-category'),
    path('category/list', views.ListCategoryView.as_view(), name='list-category')
]