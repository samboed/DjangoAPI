from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductPagination(PageNumberPagination):
    page_size = 20


class StockPagination(PageNumberPagination):
    page_size = 10


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'description']
    search_fields = ['title', 'description']
    ordering_fields = ['id', 'title']
    pagination_class = ProductPagination


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['products']
    pagination_class = StockPagination


@api_view(['GET'])
def sample_view(request):
    return Response({'message': 'Successful deploy!'})
