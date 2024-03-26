from django import forms
from .models import Coupon

class CouponApple(forms.Form):
    coupon = forms.CharField()