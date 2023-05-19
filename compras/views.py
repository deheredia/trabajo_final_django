from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Producto, Proveedor
from .forms import ProductoForm, ProveedorForm
from django.http import HttpResponseRedirect

# Create your views here.
# para crear nuestras vista, funciones y metodos para crar endpoints y asi recibir peticiones y trabajarlas

# PRIMERA VISTA

def productos_list(request):

    data = []

    productos = Producto.objects.all()

    for i in productos:

        producto = {}
        producto = {
            'nombre' : i.nombre,
            'precio' : i.precio,
            'stock_actual' : i.stock_actual,
            #'proveedor' : i.proveedor,
        }

        data.append(producto)

    return JsonResponse({'data': data})


def producto_retrieve(request, id):

    if request.method == 'GET':
        try:

            producto = Producto.objects.get(id = id)

            data = {
                'nombre' : producto.nombre,
                'precio' : producto.precio,
                'stock_actual' : producto.stock_actual,
                #'proveedor' : producto.proveedor,
            }

            return JsonResponse(data)
        
        except:
            msj = {'msj' : 'Objeto no encontrado'}

            return JsonResponse(msj)
    

def productos_filter(request, nombre):

    if request.method == 'GET':

        try:
            data = []

            productos = Producto.objects.filter(nombre = nombre)

            for i in productos:
                producto = {
                    'nombre' : i.nombre,
                    'precio' : i.precio,
                    'stock_actual' : i.stock_actual,
                    #'proveedor' : i.proveedor,
                }

                data.append(producto)

            return JsonResponse({'data' : data})
            
        except:
            msj = {'msj' : 'Objeto no encontrado'}

            return JsonResponse(msj)
        

def productos_tlistado(request):

    try:

        productos = Producto.objects.all()

        context = {
            'productos' : productos
        }
        return render(request, 'tabla_productos.jinja', context=context)
    except Exception:
        return render(request, 'error.jinja')



def create_producto(request):

    form = ProductoForm()

    if request.method == "POST":

        form = ProductoForm(request.POST)

        if form.is_valid():

            
            form.save()

            return redirect('/compras/templates/')

        else:
        
            return HttpResponseRedirect('/create_producto/')

    context = {'form': form}
    
    return render(request, 'create_producto.jinja', context)


def proveedor_tlistado(request):

    try:

        proveedores = Proveedor.objects.all()

        context = {
            'proveedores' : proveedores
        }
        return render(request, 'tabla_proveedor.jinja', context=context)
    except Exception:
        return render(request, 'error.jinja')
    


def create_proveedor(request):

    prov_form = ProveedorForm()

    if request.method == "POST":

        prov_form = ProveedorForm(request.POST)

        if prov_form.is_valid():

            
            prov_form.save()

            return redirect('/compras/proveedor')

        else:
        
            return HttpResponseRedirect('/create_proveedor/')

    context = {
        'prov_form': prov_form
        }
    
    return render(request, 'create_proveedor.jinja', context)