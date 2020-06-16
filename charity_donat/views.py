from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.views.generic.base import View
from charity_donat.models import Donation, Institution, Category
from django.db.models import Sum

class LandingPageView(View):
    def get(self,request):
        quantity_bags=Donation.objects.all().aggregate(Sum(("quantity")))
        total_quantity_bags = quantity_bags['quantity__sum']
        quantity_organizations = Donation.objects.all().aggregate(Sum(("institution")))
        total_quantity_institutions = quantity_organizations['institution__sum']
        categories=Category.objects.all()
        category_money=categories[2]
        institutions_fund=Institution.objects.filter(type=1)
        institutions_non_gov= Institution.objects.filter(type=2)
        institutions_local=Institution.objects.filter(type=3)
        for institution_fund in institutions_fund:
            for category in categories:
                institution_fund.categories.add(category)
        for institution__non_gov in institutions_non_gov:
            institution__non_gov.categories.add(category_money)
        for institution_local in institutions_local:
            institution_local.categories.add(category_money)
        return render(request,"charity_donat/index.html",{"total_quantity_bags":total_quantity_bags,
                                                          "total_quantity_institutions":total_quantity_institutions,
                                                          "institutions_fund":institutions_fund,
                                                          "institutions_non_gov":institutions_non_gov,
                                                          "institutions_local":institutions_local})

class LoginView(View):
    def get(self,request):
        return render(request,"charity_donat/login.html")
    def post(self,request):
        user=authenticate(username=request.POST.get("email"), password=request.POST.get("password"))
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return redirect("/register/#registration")

class RegisterView(View):
    def get(self,request):
        return render(request,"charity_donat/register.html")
    def post(self,request):
        first_name=request.POST.get("name")
        last_name=request.POST.get("surname")
        username = request.POST.get("email")
        password=request.POST.get("password")
        user = User.objects.create(first_name=first_name,last_name=last_name,username=username)
        user.set_password(password)
        user.save()
        return redirect("/login/")

class LogOutView(LogoutView):
    next_page = "/"


class AddDonationView(View):
    def get(self,request):
        user=request.user
        if not user.is_authenticated:
            return redirect("/login/#login-page")
        categories=Category.objects.all()
        institutions=Institution.objects.all()
        return render(request,"charity_donat/form.html",{"categories":categories,
                                                         "institutions":institutions})
    def post(self,request):
        quantity=request.POST.get("quantity")
        institution_id=request.POST.get("institution_id")
        institution=Institution.objects.get(id=institution_id)
        category_id=request.POST.get("category_id")
        category=Category.objects.get(id=category_id)
        user=request.user
        adress=request.POST.get("adress")
        city=request.POST.get("city")
        zip_code=request.POST.get("zip_code")
        phone_number=request.POST.get("phone_number")
        pick_up_date=request.POST.get("pick_up_data")
        pick_up_time=request.POST.get("pick_up_time")
        pick_up_comment=request.POST.get("pick_up_comment")

        new_donation=Donation.objects.create(quantity=quantity,adress=adress,phone_number=phone_number,
                                            city=city,zip_code=zip_code,pick_up_date=pick_up_date,
                                            pick_up_time=pick_up_time,pick_up_comment=pick_up_comment,
                                            user=user,institution=institution)
        new_donation.categories.add(category)
        return redirect("/form_confirmation/#form-confirmation")

class FormConfirmationView(View):
    def get(self,request):
        return render(request,"charity_donat/form-confirmation.html")


def get_checked(request):
    checked_cat = request.GET.get("checked_id")
    if checked_cat is not None:
        category=Category.objects.get(id=checked_cat)
        intstitutions=Institution.objects.filter(categories=category)
        return render(request, "charity_donat/rest_api_category.html", {
            "institutions": intstitutions
        })

    else:
        intstitutions=Institution.objects.all()

    return render(request,"charity_donat/form.html",{
        "institutions":intstitutions
    })



class ArchiveView(View):
    def get(self, request ):
        profile = request.user
        dotation = Donation.objects.filter(user=request.user)
        archaives = dotation.filter(is_taken=True)
        none_archived = dotation.filter(is_taken=False)
        return render(request,"charity_donat/profile.html",{"profile":profile,
                                                                    "archaives":archaives,
                                                                     "non_archaived":none_archived})
    def post(self,request):
        donation_id=request.POST.get("donation_id")
        donation=Donation.objects.get(id=donation_id)
        if donation is not None:
            if donation.is_taken==False:
                donation.is_taken=True
                donation.save()
                return redirect("/profile/#donations")
            else:
                donation.is_taken=False
                donation.save()
                return redirect("/profile/#donations")



# Create your views here.
