from django.forms import ModelForm
from .models import Order

class OrderItemForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name','last_name','city','email','address']

