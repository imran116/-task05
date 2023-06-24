
from . import views
from django.urls import path
urlpatterns = [
    path('', views.HomeView.as_view()),
    path('category/add/', views.AddCategoryView.as_view(), name='add-category'),
    path('category/list/', views.ListCategoryView.as_view(), name='list-category'),
    path('category/edit-category/<int:pk>/', views.EditCategoryView.as_view(), name='edit-category'),
    path('category/delete-category/<int:pk>/', views.DeletCategoryView.as_view(), name='delete-category'),
]