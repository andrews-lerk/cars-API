from django.utils import timezone
from rest_framework import serializers
from .utils import *
from .models import *


class ColorsSerializer(serializers.ModelSerializer):
    """ серилизатор модели цвета авто """

    class Meta:
        model = Color
        fields = "__all__"


class MarkSerializer(serializers.ModelSerializer):
    """ серилизатор модели марки авто """

    class Meta:
        model = Mark
        fields = "__all__"


class ModelsSerializer(serializers.ModelSerializer):
    """ серилизатор модели модели авто """

    class Meta:
        model = Model
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    """ серилизатор для модели заказа с переопредилением полей марки, цвета и модели авто (сделал для того чтобы
    можно было добавлять новые модели цветов, марок и моделей авто прямо из модели заказа) """

    color = serializers.CharField(max_length=31)
    mark = serializers.CharField(max_length=255)
    model = serializers.CharField(max_length=255)
    order_date = serializers.DateTimeField(allow_null=True)

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        if validated_data['order_date'] is None:
            order_date = timezone.now()
        else:
            order_date = validated_data['order_date']
        instance = Order.objects.create(
            color=get_or_create_color_model(validated_data['color']),
            mark=get_or_create_mark_model(validated_data['mark']),
            model=get_or_create_model_model(validated_data['model']),
            amount=validated_data['amount'],
            order_date=order_date
        )
        return instance

    def update(self, instance, validated_data):
        if validated_data['order_date'] is not None:
            instance.order_date = validated_data['order_date']
        instance.color = get_or_create_color_model(validated_data['color'])
        instance.mark = get_or_create_mark_model(validated_data['mark'])
        instance.model = get_or_create_model_model(validated_data['model'])
        instance.amount = validated_data['amount']
        instance.save()
        return instance
