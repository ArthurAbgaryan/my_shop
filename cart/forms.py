from django import forms

PRODUCT_QUANTITY_CHOICES = [(i,str(i)) for i in range(1,21)]
'''Форма для добавления товаров в корзину'''
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)