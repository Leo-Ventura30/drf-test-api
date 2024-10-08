from rest_framework.routers import DefaultRouter
from .viewset import VendaViewSet, ItemVendaViewSet

router = DefaultRouter()
router.register(r'vendas', VendaViewSet)
router.register(r'itens', ItemVendaViewSet)

urlpatterns = router.urls
