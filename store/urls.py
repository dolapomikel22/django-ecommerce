from django.urls import path
from . import views


urlpatterns = [
    path('', views.store, name='store'),  # Store homepage
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),  # Category filter
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),  # Product detail 
]


