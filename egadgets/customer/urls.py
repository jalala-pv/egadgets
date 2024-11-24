from django.urls import path
from .views import *

urlpatterns=[
    path('customerhome',CustomerHomeView.as_view(),name='customerhome'),
    path('products/<str:cat>',ProductListView.as_view(),name='products'),
    path('pdetail/<int:id>',ProductDetailView.as_view(),name='pdetail'),
    path('addtocart/<int:id>',addToCart,name='addtocart'),
    path('cartlist',CartListView.as_view(),name='cartlist')
]