from django.contrib import admin

from .forms import CheckoutForm
from .models import CheckoutAddress, Photo, Category, ShopCart

admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(CheckoutAddress)


class ShopCartAdmin(admin.ModelAdmin):
    list_display=['product','user','quantity','price']
    list_filter=['user']

admin.site.register(ShopCart,ShopCartAdmin)