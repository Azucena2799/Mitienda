from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from tienda.Carrito import Carrito
from tienda.models import Producto, Cliente
from tienda.modelForms import ProductoForm, ClienteForm


def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    r1 = Producto.objects.get(id=producto_id)
    r1.existencia= r1.existencia - 1
    r1.save()
    carrito.agregar(producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    r1 = Producto.objects.get(id=producto_id)
    r1.existencia= r1.existencia + 1
    r1.save()
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")

def Plantas(request):
    p = Producto.objects.all()
    context = {
        'productos': p
    }
    return render(request,'Plantas.html',context)

def AgregarPlanta(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario .is_valid():
            formulario .save()          
            return Plantas(request)
    else:
        formulario  = ProductoForm()
    return render(request,'AgregarPlanta.html',{'formulario': formulario })

def deletep(request, idr):
    try:
       r1 = Producto.objects.get(id=idr)
       r1.delete()
       return Plantas(request)
    except:
       print('')
       return Plantas(request)

def Pagar(request):
    productos = Producto.objects.all()
    return render(request, "Pagar.html", {'productos':productos})

def AgregarC (request):
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario .is_valid():
            formulario .save()          
            return Cliente(request)
    else:
        formulario  = ClienteForm()
    return render(request,'Cliente.html',{'formulario': formulario })