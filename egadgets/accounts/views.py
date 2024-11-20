from django.shortcuts import render,redirect
from django.views import View
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views.generic import TemplateView,FormView,CreateView
from django.urls import reverse_lazy

# Create your views here.

# class LandingView(View):
#     def get(self,request):
#         return render(request,'landing.html')

class LandingView(TemplateView):
    template_name='landing.html'
    
# class LoginView(View):
#     def get(self,request):
#         form=LoginForm()
#         return render(request,'login.html',{'form':form})
    # def post(self,request):
    #     form=LoginForm(data=request.POST)
    #     if form.is_valid():
    #         uname=form.cleaned_data.get('username')
    #         pswd=form.cleaned_data.get('password')
    #         user=authenticate(request,username=uname,password=pswd)
    #         if user:
    #             return redirect('customerhome')
    #         else:
    #             messages.error(request,'Login Failed!!')
    #             return redirect('login')
    #     return render(request,'login.html',{'form':form})



class LoginView(FormView):
    template_name='login.html'
    form_class=LoginForm
    def post(self,request):
        form=LoginForm(data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get('username')
            pswd=form.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            if user:
                return redirect('customerhome')
            else:
                messages.error(request,'Login Failed!!')
                return redirect('login')
        return render(request,'login.html',{'form':form})
        

# class RegistrationView(View):
#     def get(self,request):
#         form=RegistrationForm()
#         return render(request,'registration.html',{'form':form})
#     def post(self,request):
#         formdata=RegistrationForm(data=request.POST)
#         if formdata.is_valid():
#             formdata.save()
#             messages.success(request,'Registration Successfully')
#             return redirect('login')
#         messages.error(request,'Registration Failed!!')
#         return render(request,'registration.html',{'form':formdata})

class RegistrationView(CreateView):
    template_name='registration.html'
    form_class=RegistrationForm
    success_url=reverse_lazy('login')