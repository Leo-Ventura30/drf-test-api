from rest_framework.routers import DefaultRouter
from .viewset import ProdutoViewSet, GrupoProdutoViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'grupos', GrupoProdutoViewSet)

urlpatterns = router.urls
