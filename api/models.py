from django.db import models


class CapitalizeCharField(models.CharField):
    """ Переопределил чар филд чтобы в базу сохранялись однотипные записи с заглавной буквы """

    def get_prep_value(self, value):
        return str(value).capitalize()


class Color(models.Model):
    color = CapitalizeCharField('Color', max_length=31, unique=True)

    def __str__(self):
        return self.color


class Mark(models.Model):
    mark = CapitalizeCharField('Mark', max_length=255, unique=True)

    def __str__(self):
        return self.mark


class Model(models.Model):
    model = CapitalizeCharField('Model', max_length=255, unique=True)

    def __str__(self):
        return self.model


class Order(models.Model):
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING)
    mark = models.ForeignKey(Mark, on_delete=models.DO_NOTHING)
    model = models.ForeignKey(Model, on_delete=models.DO_NOTHING)
    amount = models.IntegerField('Amount')
    order_date = models.DateTimeField()
