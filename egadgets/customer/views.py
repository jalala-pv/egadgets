from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView
from accounts.models import Products,Cart
from django.contrib import messages

# Create your views here.


class CustomerHomeView(TemplateView):
    template_name='home.html'

class ProductListView(ListView):
    template_name='productlist.html'
    queryset=Products.objects.all()
    context_object_name='products'  # key name
    def get_queryset(self):
        cat=self.kwargs.get('cat')
        return self.queryset.filter(category=cat)
    
class ProductDetailView(DetailView):
    template_name='productdetail.html'
    queryset=Products.objects.all()
    context_object_name='product'
    pk_url_kwarg='id' 

def addToCart(request,*args,**kwargs):
    try:
        pid=kwargs.get('id')
        product=Products.objects.get(id=pid)
        user=request.user
        cartcheck=Cart.objects.filter(product=product,user=user).exists()
        if cartcheck:
            cartitem=Cart.objects.get(product=product,user=user)
            cartitem.quantity+=1
            cartitem.save()
            messages.success(request,'Cart Item Quantity Increased!!')
            return redirect('customerhome')
        else:
            Cart.objects.create(product=product,user=user)
            messages.success(request,f'{product.title} Added To Cart!!')
            return redirect('customerhome')
    except Exception as e:
        messages.warning(request,'Something went wrong!!!')
        return redirect('customerhome')
    
class CartListView(ListView):
    template_name='cartlist.html'
    queryset=Cart.objects.all()
    context_object_name='carts'

