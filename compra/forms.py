from django.forms import ModelForm
from .models import Proveedor, Producto

class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        
class ProveedorActualizarForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'

class ProductoForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        
class ProductoActualizarForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'