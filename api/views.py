from rest_framework import viewsets
from rest_framework.views import APIView, Response
from rest_framework.pagination import PageNumberPagination
from .utils import get_count_from_colors, get_count_from_marks

from .serializers import *


class OrderAPIListPagination(PageNumberPagination):
    """ пагинатор для модели заказа """

    page_size = 10


class ColorsViewSet(viewsets.ModelViewSet):
    """ CRUD для модели цвета """

    queryset = Color.objects.all()
    serializer_class = ColorsSerializer


class MarkViewSet(viewsets.ModelViewSet):
    """ CRUD для модели марки """

    queryset = Mark.objects.all()
    serializer_class = MarkSerializer


class ModelsViewSet(viewsets.ModelViewSet):
    """ CRUD для модели модели авто """

    queryset = Model.objects.all()
    serializer_class = ModelsSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """ CRUD для модели заказа """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = OrderAPIListPagination

    def get_queryset(self):
        queryset = Order.objects.all()
        mark = self.request.query_params.get('mark')
        amount = self.request.query_params.get('amount')
        if mark is not None:
            queryset = queryset.filter(mark__mark=mark)
        if amount is not None:
            queryset = queryset.order_by('amount')
        return queryset


class CountFromColorsAPIListView(APIView):
    """ список цветов с указанием количества заказанных авто каждого цвета (атрибуты элементов: цвет, количество) """

    def get(self, request):
        queryset = Color.objects.all()
        result = get_count_from_colors(queryset)
        return Response({'result': result})


class CountFromMarksAPIListView(APIView):
    """ список марок с указанием количества заказанных авто каждой марки (атрибуты элементов: марка, количество) """

    def get(self, request):
        queryset = Mark.objects.all()
        result = get_count_from_marks(queryset)
        return Response({'result': result})
