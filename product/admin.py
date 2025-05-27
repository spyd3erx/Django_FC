from django.contrib import admin
from .models import Products, ProductImages


# Modificando el encabezado
admin.site.site_header = "3DShop Administration"

# Modificando el título de la página de inicio
admin.site.index_title = "Panel de Control"


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "description", "price",  "stock", "created_at")
    ordering = ("-product_name",)

@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    pass