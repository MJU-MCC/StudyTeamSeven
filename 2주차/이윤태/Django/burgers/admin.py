from django.contrib import admin
from burgers.models import Burger #models.py에 있는 Burger클래스

@admin.register(Burger)
class BurgerAdmin(admin.ModelAdmin):
    pass
# Register your models here.
