from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    # Your other URL patterns here
    path('', views.home, name='home'),
    path('index/', views.index_view, name='index'),
    path('register/', views.register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

