from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet, FornecedorViewSet

router = DefaultRouter()
<<<<<<< HEAD
router.register(r'produtos', ProdutoViewSet, basename='produto')
router.register(r'fornecedores', FornecedorViewSet, basename='fornecedor')
=======
router.register(r'produtos', ProdutoViewSet, basename='produtos')
>>>>>>> 2354bce917e52466985306ed75794a548657b500

urlpatterns = [
    path('', include(router.urls)),
]