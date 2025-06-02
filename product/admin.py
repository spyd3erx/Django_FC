from django.contrib import admin
from .models import Products, ProductImages
from import_export.admin import ImportExportMixin
from .ProductResource import ProductResource



# Modificando el encabezado
admin.site.site_header = "3DShop Administration"

# Modificando el título de la página de inicio
admin.site.index_title = "Panel de Control"


@admin.register(Products)
class ProductAdmin(ImportExportMixin, admin.ModelAdmin):
    #resource
    resource_classes = [ProductResource]
    search_fields = ("product_name",)
    list_display = ["product_name", "price",  "stock", "created_at", "status"]
    ordering = ("-product_name",)


@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ["product", "color"]