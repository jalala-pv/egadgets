from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Create your views here.

# class CustomerHomeView(View):
#     def get(self,request):
#         return render(request,'home.html')

class CustomerHomeView(TemplateView):
    template_name='home.html'