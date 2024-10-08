from rest_framework import viewsets
from .models import Produto, GrupoProduto
from .serializers import ProdutoSerializer, GrupoProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class GrupoProdutoViewSet(viewsets.ModelViewSet):
    queryset = GrupoProduto.objects.all()
    serializer_class = GrupoProdutoSerializer
