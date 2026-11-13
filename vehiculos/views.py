from rest_framework import viewsets

from .models import Vehiculo
from .serializers import VehiculoSerializer


class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

    def get_view_name(self):
        return 'Vehículos' if self.detail is False else 'Vehículo'
