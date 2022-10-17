from .models import *
from django.core.exceptions import ObjectDoesNotExist


def get_or_create_color_model(color: str):
    """ получает или создает модель цвета """

    normalize_color = color.capitalize()
    try:
        instance = Color.objects.get(color=normalize_color)
    except ObjectDoesNotExist:
        instance = Color.objects.create(color=normalize_color)
    return instance


def get_or_create_mark_model(mark: str):
    """ получает или создает модель марки """

    normalize_mark = mark.capitalize()
    try:
        instance = Mark.objects.get(mark=normalize_mark)
    except ObjectDoesNotExist:
        instance = Mark.objects.create(mark=normalize_mark)
    return instance


def get_or_create_model_model(model: str):
    """ получает или создает модель модели авто """

    normalize_model = model.capitalize()
    try:
        instance = Model.objects.get(model=normalize_model)
    except ObjectDoesNotExist:
        instance = Model.objects.create(model=normalize_model)
    return instance


def get_count_from_colors(queryset):
    """ алгоритм получения списка цветов с указанием количества заказанных авто каждого цвета """

    result = []
    for color_instance in queryset:
        count_of_cars = 0
        order_queryset = Order.objects.filter(color=color_instance)
        for order_instance in order_queryset:
            count_of_cars+=order_instance.amount
        result.append({
            'color': color_instance.color,
            'amount': count_of_cars
        })
    return result


def get_count_from_marks(queryset):
    """ алгоритм получения списка марок с указанием количества заказанных авто каждой марки """

    result = []
    for mark_instance in queryset:
        count_of_cars = 0
        order_queryset = Order.objects.filter(mark=mark_instance)
        for order_instance in order_queryset:
            count_of_cars+=order_instance.amount
        result.append({
            'mark': mark_instance.mark,
            'amount': count_of_cars
        })
    return result
