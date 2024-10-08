from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_email(self, value):
        if Cliente.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email já está cadastrado.")
        return value

    def validate_telefone(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("O número de telefone deve ter no mínimo 10 dígitos.")
        return value