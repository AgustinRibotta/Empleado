
from django.urls import path
from .views import *

urlpatterns = [
    path('home/',IndexView.as_view()),
    path('resumen/',ResumenFundationView.as_view()),
    path('lista/',PruebaListView.as_view()),
    path('listaPrueba/',ModeloPruebaListView.as_view()),
    path('addprueba/',PruebaCreateView.as_view(),name='add'),

]
