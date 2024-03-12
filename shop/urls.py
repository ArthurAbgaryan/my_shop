from django.urls import path
from . import views
app_name = 'shop'

urlpatterns = [
    path('',views.list_products, name = 'product_list'),
    path('<slug:category_slug>/', views.list_products, name = 'product_list_b_category'),
    path('product_detail/<int:pk>/<slug:slug>/', views.products_detail, name = 'product_detail'),
]