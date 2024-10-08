from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Venda, ItemVenda
from .serializers import VendaSerializer, ItemVendaSerializer
from .service import VendaService

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all().select_related('cliente', 'vendedor').prefetch_related('itens__produto')
    serializer_class = VendaSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        cliente = request.data['cliente']
        vendedor = request.data['vendedor']
        itens = request.data['itens']
        venda = VendaService.criar_venda(cliente, vendedor, itens)
        return Response({'venda_id': venda.id})

    def retrieve(self, request, *args, **kwargs):
        try:
            venda = self.get_object()
            serializer = self.get_serializer(venda)
            return Response(serializer.data)
        except NotFound:
            return Response({'error': 'Venda não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': 'Erro ao buscar venda'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ItemVendaViewSet(viewsets.ModelViewSet):
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer
