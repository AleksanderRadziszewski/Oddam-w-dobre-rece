from django.db import models
from django.contrib.auth.models import User

fundacja=1
organizacja_pozarzadowa=2
zbiorka_lokalna=3

institution_type=[
    (fundacja,"fundacja"),
    (organizacja_pozarzadowa,"organizacja_pozarządowa"),
    (zbiorka_lokalna,"zbiórka lokalna"),

]

class Category(models.Model):
    name=models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Institution(models.Model):
    name = models.CharField(max_length=40)
    description=models.TextField()
    type=models.CharField(max_length=40,choices=institution_type,default=fundacja)
    categories=models.ManyToManyField(Category)

    def __str__(self):
        return self.name

class Donation(models.Model):
    quantity=models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution=models.ForeignKey(Institution,on_delete=models.CASCADE)
    adress=models.CharField(max_length=80)
    phone_number=models.IntegerField()
    city=models.CharField(max_length=20)
    zip_code=models.CharField(max_length=12)
    pick_up_date=models.DateField()
    pick_up_time=models.DateTimeField()
    pick_up_comment=models.TextField()
    user=models.OneToOneField(User, on_delete=models.CASCADE)




# Create your models here.
