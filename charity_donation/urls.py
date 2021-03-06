"""charity_donation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from charity_donat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.LandingPageView.as_view(), name="landing_page"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("add_donation/", views.AddDonationView.as_view(), name="add_donation"),
    path("get_institutions/", views.get_checked, name="get_checked"),
    path("form_confirmation/", views.FormConfirmationView.as_view(), name="form_confirmation"),
    path("profile/", views.ArchiveView.as_view(), name="profile"),
    path("profile_edit/", views.ProfileEditView.as_view(), name="profile_edit"),
    path("change_password/", views.ChangePasswordView.as_view(), name="change_password"),
    path("send_link_change_password/", views.LinkToChangePasswordView.as_view(), name="link_change_password"),
    path("pagination_fund/", views.PaginationView.as_view(), name="pagination_fund"),
    path("check_email/",views.CheckingEmailView.as_view(),name="check_email"),
    path("activate/<uidb64>/<token>/", views.VeryficationRegisterView.as_view(), name="activate"),

]
