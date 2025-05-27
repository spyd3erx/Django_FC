from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path("", views.ProductsView.as_view(), name="index"),
    path("detail/<int:pk>/", views.ProductDetail.as_view(), name="detail"),
    
]