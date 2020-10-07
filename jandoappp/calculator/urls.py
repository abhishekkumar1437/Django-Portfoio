from django.urls import path
from . import views

urlpatterns = [
    path('calculators/',views.calculator, name='calculator'),
]