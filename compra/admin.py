from django.contrib import admin
from compra.models import Producto, Proveedor

# Register your models here.

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'dni')
    
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'stock_actual', 'proveedor')
