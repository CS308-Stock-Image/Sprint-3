from django.contrib import admin
from .models import Photo, Category, ShopCart

admin.site.register(Category)
admin.site.register(Photo)

class ShopCartAdmin(admin.ModelAdmin):
    list_display=['product','user','quantity','price']
    list_filter=['user']

admin.site.register(ShopCart,ShopCartAdmin)