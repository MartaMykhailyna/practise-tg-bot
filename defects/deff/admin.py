from django.contrib import admin
from .models import User, Order, Admin, Defect

# Register your models here.
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Admin)
admin.site.register(Defect)