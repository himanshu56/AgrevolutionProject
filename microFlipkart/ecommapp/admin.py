from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserModel)
admin.site.register(ProductVariantModel)
admin.site.register(ProductModel)
admin.site.register(VariantModel)
admin.site.register(OrderModel)