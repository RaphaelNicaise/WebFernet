from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.ListarProductos.as_view(), name='lista_productos'),
    path('productos/<int:id>/', views.ListarProducto.as_view(), name='lista_producto'),
]
