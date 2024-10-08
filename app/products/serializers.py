from rest_framework import serializers
from .models import Produto, GrupoProduto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

    def validate_preco(self, value):
        if value <= 0:
            raise serializers.ValidationError("O preço deve ser maior que zero.")
        return value

    def validate_grupo(self, value):
        if not value:
            raise serializers.ValidationError("O grupo de produto é obrigatório.")
        return value

class GrupoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoProduto
        fields = '__all__'
