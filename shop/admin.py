from django.contrib import admin
from .models import Category,Product

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name','slug','price','available','date_created','update']
    list_filter = ['available','date_created','update']
    list_editable = ['price','available']#поз-ет изменять  прямо в списке товаров не прибегая к редактировнию
    prepopulated_fields = {'slug':('name',)}
# Register your models here.
