from django.shortcuts import render
from django.views.generic.base import View


class LandingPageView(View):
    def get(self,request):
        return render(request,"charity_donat/index.html")

class LoginView(View):
    def get(self,request):
        return render(request,"charity_donat/login.html")

class RegisterView(View):
    def get(self,request):
        return render(request,"charity_donat/register.html")

class AddDonationView(View):
    def get(self,request):
        return render(request,"charity_donat/form.html")

# Create your views here.
