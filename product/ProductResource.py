from import_export import resources
from .models import Products

class ProductResource(resources.ModelResource):
    
    class Meta:
        model = Products
        # Campos a incluir (opcional, si no se especifica, incluye todos)
        fields = ["id", "product_name", "sku", "stock", "description", "price", "created_at", "imagen", "status"]
        
    
        # # Campos para excluir (opcional)
        # exclude = ('campo_no_deseado',)
        # # Para ordenar los campos en el export
        # export_order = ('id', 'campo1', 'campo2')