from datetime import date

from rest_framework import serializers

from .models import Vehiculo


class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['id', 'marca', 'modelo', 'anio', 'color', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'marca': {'error_messages': {'required': 'La marca es obligatoria.', 'blank': 'La marca no puede estar vacía.'}},
            'modelo': {'error_messages': {'required': 'El modelo es obligatorio.', 'blank': 'El modelo no puede estar vacío.'}},
            'anio': {'error_messages': {'required': 'El año es obligatorio.', 'invalid': 'El año debe ser un número entero.'}},
            'color': {'error_messages': {'required': 'El color es obligatorio.', 'blank': 'El color no puede estar vacío.'}},
        }

    def validate_anio(self, value):
        maximo = date.today().year + 1
        if value < 1886 or value > maximo:
            raise serializers.ValidationError(f'El año debe estar entre 1886 y {maximo}.')
        return value
