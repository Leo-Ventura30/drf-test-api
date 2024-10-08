from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.permissions import IsAuthenticated
from .models import Cliente
from .serializers import ClienteSerializer
import logging

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            logger.error(f"Erro ao criar cliente: {e}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Erro interno: {e}")
            return Response({'error': 'Erro interno ao criar cliente'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': 'Erro ao listar clientes'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        try:
            cliente = self.get_object()
            serializer = self.get_serializer(cliente)
            return Response(serializer.data)
        except NotFound:
            return Response({'error': 'Cliente não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': 'Erro ao buscar cliente'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)