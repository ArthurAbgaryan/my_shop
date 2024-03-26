from django.shortcuts import render,redirect
from .models import Coupon
from .forms import CouponApple
from django.views.decorators.http import require_POST
from django.utils import timezone

@require_POST
def coupon(request):
    form = CouponApple(request.POST)
    now_time = timezone.now()
    if form.is_valid():
        code_coupon = form.cleaned_data['coupon']
        try:
            coupon = Coupon.objects.get(
                code__iexact= code_coupon,
                valid_from__lte = now_time,
                valid_to__gte = now_time,
                active = True
            )
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None

    return redirect ('cart:cart_detail')


# Create your views here.
