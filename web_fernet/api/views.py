from rest_framework import generics
from productos.models import Producto

from .serializers import ProductoSerializer

class ListarProductos(generics.ListAPIView):
    """
    API para listar y crear productos.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
class ListarProducto(generics.RetrieveAPIView):
    """
    API para obtener un producto específico.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field = 'id' 
    