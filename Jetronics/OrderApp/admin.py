from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(MissingOrder)
admin.site.register(OrderModel)
admin.site.register(OrderSettingsModel)