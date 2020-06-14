from django.contrib import admin

from charity_donat.models import Institution,Category,Donation

admin.site.register(Institution)
admin.site.register(Donation)
admin.site.register(Category)
# Register your models here.
