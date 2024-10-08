from .models import Venda, ItemVenda

class VendaService:
    @staticmethod
    def criar_venda(cliente, vendedor, itens):
        venda = Venda.objects.create(cliente=cliente, vendedor=vendedor)
        for item in itens:
            ItemVenda.objects.create(venda=venda, produto=item['produto'], quantidade=item['quantidade'], preco_unitario=item['preco_unitario'])
        return venda