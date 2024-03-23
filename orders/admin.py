from django.contrib import admin
from .models import Order,OrderItem
from django.utils.safestring import mark_safe
from django.shortcuts import reverse

def order_view(obj):
    return mark_safe('<a href="{}">View</a>'.format(reverse('order:admin_detail', args=[obj.id])))
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'first_name',
                    'last_name',
                    'email','address','postal_code',
                    'city','paid','created','update', order_view]
    list_filter = ['paid','created','update']
    inlines = [OrderItemInline]
# Register your models here.
