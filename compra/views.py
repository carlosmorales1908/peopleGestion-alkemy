from django.shortcuts import redirect, render
from compra.forms import ProductoForm, ProveedorForm
from compra.models import Producto, Proveedor
# Create your views here.


def home(request):
    return render(request, 'index.html')

                                #views Proveedores
def proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'listado-empleados.html', {'proveedores': proveedores})

def campos_validos_proveedor(formulario):
    return formulario.cleaned_data['nombre'].isalpha() and formulario.cleaned_data['apellido'].isalpha() and formulario.cleaned_data['dni'].isnumeric()

def crear_proveedor(request):
    form = ProveedorForm()
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid() and campos_validos_proveedor(form):
            form.save()
            return redirect('proveedores')
    return render(request, 'crear-actualizar-proveedor.html', {'form': form, 'submit': 'Crear empleado'})


                                #views Productos
def productos(request):
    productos = Producto.objects.all()
    return render(request, 'listado-empleados.html', {'producto': productos})

def crear_producto(request):
    form = ProductoForm()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')
    return render(request, 'crear-actualizar-producto.html', {'form': form, 'submit': 'Crear producto'})