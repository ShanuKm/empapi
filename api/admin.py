from django.contrib import admin
from .models import Emp

# Register your models here.
@admin.register(Emp)
class EmpAdmin(admin.ModelAdmin):
    list_display =['id','name','phone', 'address','department']
