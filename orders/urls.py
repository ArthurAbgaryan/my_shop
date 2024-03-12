from . import views
from django.urls import path
app_name = 'order'

urlpatterns = [
    path('create/', views.create_order, name = 'create_order'),
]