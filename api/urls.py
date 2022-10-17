from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register('colors', ColorsViewSet)
router.register('marks', MarkViewSet)
router.register('models', ModelsViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('from_colors_count', CountFromColorsAPIListView.as_view()),
    path('from_mark_count', CountFromMarksAPIListView.as_view())
]