from accounts.models import Orders,Cart

def item_count(request):
    if request.user.is_authenticated:
        cart_count=Cart.objects.filter(user=request.user).count()
        order_count=Orders.objects.filter(user=request.user).count()
        return {'order':order_count,'cart':cart_count}
    else:
        return {"order":0,"cart":0}