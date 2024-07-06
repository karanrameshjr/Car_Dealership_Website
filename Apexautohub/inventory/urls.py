from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.inventory_view, name='inventory'),
    path('brand1/', views.brand1_view, name='brand1'),
    path('tata1/', views.tata1_view, name='tata1'),
    path('tata2/', views.tata2_view, name='tata2'),
    path('tata3/', views.tata3_view, name='tata3'),
    path('tata4/', views.tata4_view, name='tata4'),
    path('tata5/', views.tata5_view, name='tata5'),
    path('brand2/', views.brand2_view, name='brand2'),
    path('toyota1/', views.toyota1_view, name='toyota1'),
    path('toyota2/', views.toyota2_view, name='toyota2'),
    path('toyota3/', views.toyota3_view, name='toyota3'),
    path('toyota4/', views.toyota4_view, name='toyota4'),
    path('toyota5/', views.toyota5_view, name='toyota5'),
    path('toyota6/', views.toyota6_view, name='toyota6'),
    path('brand3/', views.brand3_view, name='brand3'),
    path('benz1/', views.benz1_view, name='benz1'),
    path('benz2/', views.benz2_view, name='benz2'),
    path('benz3/', views.benz3_view, name='benz3'),
    path('benz4/', views.benz4_view, name='benz4'),
    path('benz5/', views.benz5_view, name='benz5'),
    path('brand4/', views.brand4_view, name='brand4'),
    path('kia1/', views.kia1_view, name='kia1'),
    path('kia2/', views.kia2_view, name='kia2'),
    path('kia3/', views.kia3_view, name='kia3'),
    path('kia4/', views.kia4_view, name='kia4'),
    path('brand5/', views.brand5_view, name='brand5'),
    path('audi1/', views.audi1_view, name='audi1'),
    path('audi2/', views.audi2_view, name='audi2'),
    path('audi3/', views.audi3_view, name='audi3'),
    path('audi4/', views.audi4_view, name='audi4'),
    path('audi5/', views.audi5_view, name='audi5'),
    path('brand6/', views.brand6_view, name='brand6'),
    path('ms1/', views.ms1_view, name='ms1'),
    path('ms2/', views.ms2_view, name='ms2'),
    path('ms3/', views.ms3_view, name='ms3'),
    path('ms4/', views.ms4_view, name='ms4'),
    path('ms5/', views.ms5_view, name='ms5'),


    # Add more URL patterns as needed for other views
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

