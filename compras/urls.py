from django.urls import path
from . import views

urlpatterns = [
    # path('productos/', views.productos_list),
    # path('productos/<int:id>/', views.producto_retrieve), 
    # path('productos/<str:nombre>/', views.productos_filter),
    path('templates/', views.productos_tlistado),
    path('templates/create_producto/', views.create_producto, name='create_producto'),
    path('', views.proveedor_tlistado),
    path('proveedor/', views.create_proveedor),

]