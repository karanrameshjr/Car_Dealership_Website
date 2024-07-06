from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.inventory_view, name='inventory'),
    path('brand1/', views.brand1_view, name='brand1'),
    path('tata1/', views.tata1_view, name='tata1'),
    path('tata2/', views.tata2_view, name='tata2'),
    # Add more URL patterns as needed for other views
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

