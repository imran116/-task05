
from . import views
from django.urls import path
urlpatterns = [
    path('', views.HomeView.as_view()),
    path('category/add/', views.AddCategoryView.as_view(), name='add-category'),
    path('category/list/', views.ListCategoryView.as_view(), name='list-category'),
    path('category/edit-category/<int:pk>/', views.EditCategoryView.as_view(), name='edit-category'),
    path('category/delete-category/<int:pk>/', views.DeleteCategoryView.as_view(), name='delete-category'),
    path('product/list/', views.ListProductView.as_view(), name='list-product'),
    path('product/add/', views.AddProductView.as_view(), name='add-product'),
    path('product/edit-product/<int:pk>/', views.EditProductView.as_view(), name='edit-product'),
    path('product/delete-product/<int:pk>/', views.DeleteProductView.as_view(), name='delete-product'),
]