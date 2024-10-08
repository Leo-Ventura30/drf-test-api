from rest_framework import serializers
from .models import Venda, ItemVenda

class ItemVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVenda
        fields = '__all__'
        
class VendaSerializer(serializers.ModelSerializer):
    itens = ItemVendaSerializer(many=True)
    
    class Meta:
        model = Venda
        fields = '__all__'
        
    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        venda = Venda.objects.create(**validated_data)
        for item_data in itens_data:
            ItemVenda.objects.create(venda=venda, **item_data)
        return venda
    