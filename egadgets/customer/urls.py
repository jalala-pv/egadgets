from django.urls import path
from .views import *

urlpatterns=[
    path('customerhome',CustomerHomeView.as_view(),name='customerhome')
]