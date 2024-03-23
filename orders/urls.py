from . import views
from django.urls import path
app_name = 'order'

urlpatterns = [
    path('create/', views.create_order, name = 'create_order'),
    path('admin/order/<int:order_id>/', views.admin_ite, name = 'admin_detail'),

]