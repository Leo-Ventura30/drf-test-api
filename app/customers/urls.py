from rest_framework.routers import DefaultRouter
from .viewset import ClienteViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)

urlpatterns = router.urls
