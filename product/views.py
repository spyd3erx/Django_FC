from typing import Any
from django.shortcuts import render
from django.views import generic

from .models import Products


class ProductsView(generic.ListView):
    queryset = (
        Products.objects.filter(status=True)
        .order_by("product_name")
        .defer("created_at", "updated_at", "deleted_at")
    )
    # template_name = "custom_template.html"
    context_object_name = "products"


class ProductDetail(generic.DetailView):
    model = Products
    context_object_name = "product"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.prefetch_related("images")
