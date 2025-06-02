from django.db import models
from django.utils import timezone
from django.db.models import Q
from django.core.validators import MinLengthValidator, MinValueValidator

#Custom Manager
class ProductManager(models.Manager):
    def without_stock(self):
        filter_by_stock = Q(stock=0)
        is_active = Q(status=True)
        return self.filter(filter_by_stock & is_active)


class Products(models.Model):
    product_name = models.CharField(max_length=50, unique=True)
    sku = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(
                10, message="El campo debe contener al solo 10 caracteres."
            )
        ],
    )
    stock = models.IntegerField(
        validators=[MinValueValidator(1, message="El stock minimo debe ser de 1")]
    )
    description = models.TextField()
    imagen = models.ImageField(null=True, blank=True, upload_to="products")
    price = models.DecimalField(max_digits=9, decimal_places=2)
    created_at = models.DateField(
        auto_now_add=True
    )  # registra la fecha en la que se creo el registro
    updated_at = models.DateField(
        auto_now=True
    )  # registra la fecha cada vez que se modifica el registro
    status = models.BooleanField(default=True)
    deleted_at = models.DateField(default=timezone.now)

    # meta info
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self) -> str:
        return self.product_name

    #Base Manager
    objects = models.Manager()
    
    #custom Manager
    product = ProductManager()

class ProductImages(models.Model):
    #el paremetro related_name, sustituye al _set, creando una relación con el objeto más natural
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to=f"variaciones")
    color = models.CharField(null=False, max_length=20)

    # meta info
    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"

    def __str__(self) -> str:
        return str(self.product)
